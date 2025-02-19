import sys
import os
# Get the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Append the 'sedmlEditor' directory to the system path
sys.path.append(os.path.join(current_dir, '../sedmlEditor/'))
from sedDict import create_dict_sedDocment, add_peTask2dict
from sedEditor import create_sedDocment,write_sedml, validate_sedml

def pe_task():

    # ********** The following is to create a dictionary for the sedml file **********
    dict_sedDocument=create_dict_sedDocment()
    # This is the sedml file (relative) path and name, assuming in the same folder with the CellML model file
    path_='../models/'
    model_path ='./'
    model_name='NKE_pump_BG_4states'
    model_id = model_name # This is the model id in the sedml, could be different from the model file name
    sedFilename = model_name+'_pe_fit2.sedml' 
    full_path = path_+ sedFilename 
    ss_time={50} # The time for the steady state, if not provided, the default value will be used
    cost_type='AE' 
    # The cost function type, could be 'AE' (absolute error),
    # 'MIN-MAX' (normalized by (max(exp_value)-min(exp_value))), 
    # 'Z-SCORE' (normalized by std(exp_value), 
    # or 'MSE' (mean squared error). 

    # ********** The following is to add the task information to the dictionary **********

    # Note: the following is an example, you can modify it to add more tasks
    # Note: the valid sedml id should start with a letter, and only contain letters, numbers, and underscores

    # This is the model id in the sedml file, which is also the task id and output id
    model_names=[model_id]
    # This is the model file name, assuming in the same folder with the sedml file
    model_sources=[model_path+ model_name+'.cellml']
    # This is to set optimization algorithm
    # This is to set the tolerance for least square when using local optimization algorithm, default is 1e-8
    dict_algorithmParameter_opt={'kisaoID':'KISAO:0000597','name':'tol','value':'1e-6'} 
    # This is to set the maximum number of iterations when using local optimization algorithm, default is 1000
    dict_algorithmParameter_opt2={'kisaoID':'KISAO:0000486','name':'maxiter','value':'2000'} 

    # ****************** You can choose one of the following optimization algorithms ******************
    # This is to set optimization algorithm as local optimization algorithm, and the scipy.least_square is implemented in the code
    dict_algorithm_opt={'kisaoID':'KISAO:0000520','name':'evolutionary algorithm', 'listOfAlgorithmParameters':[dict_algorithmParameter_opt,dict_algorithmParameter_opt2]}

    # This is to set optimization algorithm as global optimization algorithm, and scipy.shgo is used to implement the algorithm
    # dict_algorithm_opt={'kisaoID':'KISAO:0000472','name':'global optimization algorithm', 'listOfAlgorithmParameters':[dict_algorithmParameter_opt,dict_algorithmParameter_opt2]}

    # This is to set optimization algorithm as genetic algorithm, and scipy.differential_evolution is used to implement the algorithm
    # dict_algorithm_opt={'kisaoID':'KISAO:0000520','name':'evolutionary algorithm', 'listOfAlgorithmParameters':[dict_algorithmParameter_opt,dict_algorithmParameter_opt2]}

    # This is to set optimization algorithm as simulated annealing, and scipy.dual_annealing is used to implement the algorithm
    # dict_algorithm_opt={'kisaoID':'KISAO:0000503','name':'simulated annealing', 'listOfAlgorithmParameters':[dict_algorithmParameter_opt,dict_algorithmParameter_opt2]}

    # This is to set optimization algorithm as random search, and scipy.basinhopping is used to implement the algorithm
    # Note: basinhopping does not support bounds, and the bounds will be ignored
    # dict_algorithm_opt={'kisaoID':'KISAO:0000504','name':'random search', 'listOfAlgorithmParameters':[dict_algorithmParameter_opt,dict_algorithmParameter_opt2]}

    # ***************** This is to set simulation algorithms *****************
    # This is to set the maximum step size for the simulation
    dict_algorithmParameter={'kisaoID':'KISAO:0000209', 'name':'rtol','value':'1e-9'} 
    dict_algorithmParameter2={'kisaoID':'KISAO:0000211', 'name':'atol','value':'1e-9'}
    dict_algorithmParameter3={'kisaoID':'KISAO:0000467', 'name':'max_step','value':'0.00001'} 
    dict_algorithmParameter4={'kisaoID':'KISAO:0000475', 'name':'method','value':'bdf'} 
    # You can set more algorithm parameters if needed. You can refer to get_KISAO_parameters() in src/simulator.py file to get the parameters for the specific algorithm
    # Add the algorithm parameters to listOfAlgorithmParameters
    # You can choose one of the simulation algorithms specified by KISAO_ALGORITHMS in src/simulator.py file
    # dict_algorithm_sim={'kisaoID':'KISAO:0000030','name':'Euler forward method', 'listOfAlgorithmParameters':[dict_algorithm_sim_parameter]}
    dict_algorithm_sim={'kisaoID':'KISAO:0000088','name':'LSODA', 'listOfAlgorithmParameters':[dict_algorithmParameter,dict_algorithmParameter2]}
    dict_algorithm_sim={'kisaoID':'KISAO:0000088','name':'LSODA', 'listOfAlgorithmParameters':[dict_algorithmParameter,dict_algorithmParameter2]}
    #dict_algorithm_sim={'kisaoID':'KISAO:0000535','name':'VODE', 'listOfAlgorithmParameters':[dict_algorithmParameter,dict_algorithmParameter2,dict_algorithmParameter4]}


    # ******************** This is to modify the model parameters if needed ********************
    changes={'z1':{'component':'main','name':'z_1','newValue':'-0.054951'}} # by default, no changes to the model parameters
    # the format is {'id':{'component':str,'name':str,'newValue':str}}
    # Example: changes={'v_CO2_max':{'component':'main','name':'v_CO2_max','newValue':'10'}

    # ******************** This is to specify the data source files for the fitting experiments ********************
    # The data source file should be in the same folder with the sedml file, otherwise, the full path should be provided

    # Specify the data source file for the expected observables, which is used for fitting. This is a must.
    data_observables_Nai='../data/Terkildsen_NaK_kinetic_Nai_cond.csv'
    data_observables_Ke='../data/Terkildsen_NaK_kinetic_Ke_cond.csv'
    data_observables_ATP='../data/Terkildsen_NaK_kinetic_ATP_cond.csv'
    data_observables_volt='../data/Terkildsen_NaK_kinetic_volt_cond.csv'
    fileId_observable='cond_Nai'
    fileId_observable2='cond_Ke'
    fileId_observable3='cond_ATP'
    fileId_observable4='cond_volt'

    experimentData_files={fileId_observable:{'data_summary':'expected_observables_Nai','data_file':data_observables_Nai,'observables':{},'experimentalConditions':{}},
                          fileId_observable2:{'data_summary':'expected_observables_Ke','data_file':data_observables_Ke,'observables':{},'experimentalConditions':{}},
                          fileId_observable3:{'data_summary':'expected_observables_ATP','data_file':data_observables_ATP,'observables':{},'experimentalConditions':{}},
                        fileId_observable4:{'data_summary':'expected_observables_volt','data_file':data_observables_volt,'observables':{},'experimentalConditions':{}}
                        }
    # time
    # format: [dataSourceId,column_name,startIndex,endIndex,component,name]
    # column_name: the column name in the data source file corresponding to the time points
    # startIndex: the start index of the time points, default is None
    # endIndex: the end index of the time points, default is None
    # component: the component name in the model where the variable of integration is located
    # name: the name of the variable of integration in the model
   # dataSourceId_0='time'
   # time={dataSourceId_0:{'column_name':'t','startIndex':101,'endIndex':None,'component':'main','name':'t'}} 
    # if the fitting experiment is steady state, the time is not needed. time={}
    # if the fitting experiment is steady state, time_map=()
    time_map=()
    # observables
    # format: [dataSourceId,column_name,startIndex,endIndex,component,name,weight]
    # column_name: the column name in the data source file corresponding to the measured observable data
    # startIndex: the start index of the observable, default is None
    # endIndex: the end index of the observable, default is None
    # component: the component name in the model where the observable variable is located
    # name: the name of the observable variable in the model
    # weight: the weight for the observable, default is 1
    dataSourceId_1='v_ss_Nai'
    obs1=[dataSourceId_1,'v_ss',None,None,'main','v_1',1]
    dataSourceId_2='v_ss_Ke'
    obs2=[dataSourceId_2,'v_ss',None,None,'main','v_1',1]
    dataSourceId_3='v_ss_ATP'
    obs3=[dataSourceId_3,'v_ss',None,None,'main','v_1',1]
    dataSourceId_4='v_ss_volt'
    obs4=[dataSourceId_4,'v_ss',None,None,'main','v_1',1]
    # You can add more observables if needed
    # Add the observables to the list
    observables=[obs1,obs2,obs3,obs4]

    #observables_map=[(fileId,dataSourceId,'function for observable output, default is the var with '', abs(var), or-(var),')] to map the data source file and the data source
    observables_map =[(fileId_observable,dataSourceId_1,'')]
    observables_map2 =[(fileId_observable2,dataSourceId_2,'')]
    observables_map3 =[(fileId_observable3,dataSourceId_3,'')]
    observables_map4 =[(fileId_observable4,dataSourceId_4,'')] 
    
    #zip experimentData_files and observables
    fileId_observables=[fileId_observable,fileId_observable2,fileId_observable3,fileId_observable4]
    observables=[obs1,obs2,obs3,obs4]
    zipped_observables = zip(fileId_observables, observables)
    for fid, obs in zipped_observables:
        dataSourceId=obs[0]
        column_name=obs[1]
        startIndex=obs[2]
        endIndex=obs[3]
        component=obs[4]
        name=obs[5]
        weight=obs[6]
        experimentData_files[fid]['observables'][dataSourceId]={'column_name':column_name,'startIndex':startIndex,'endIndex':endIndex,'component':component,'name':name, 'weight':weight}  

    # Specify the data source file for the experiment conditions if external input is needed. Otherwise, you don't need to specify it.
    # data_source_file1='report_task_Boron_CO2.csv'
    # fileId1='conditions'
    # data_summary_1='conditions'
    # experimentalConditions
    # format: [dataSourceId,column_name,startIndex,endIndex,index_value,component,name]
    # column_name: the column name in the data source file corresponding to the experimental condition
    # startIndex: the start index of the experimental condition, default is None
    # endIndex: the end index of the experimental condition, default is None
    # index_value: the value of the experimental condition, default is None
    # component: the component name in the model where the experimental condition variable is located
    # name: the name of the experimental condition variable in the model
    # You can add more experimental conditions if needed
    # e.g.,
    # dataSourceId_2='q_CO2_i'
    # exp1=[dataSourceId_2,'J_CO2_i',None,None,None,'main','q_CO2_i']
    dataSourceId_cond='c_Nai'
    exp1=[dataSourceId_cond,'c_Nai',None,None,None,'main','c_Nai']
    dataSourceId_cond2='c_Nae'
    exp2=[dataSourceId_cond2,'c_Nae',None,None,None,'main','c_Nae']
    dataSourceId_cond3='c_Ki'
    exp3=[dataSourceId_cond3,'c_Ki',None,None,None,'main','c_Ki']
    dataSourceId_cond4='c_Ke'
    exp4=[dataSourceId_cond4,'c_Ke',None,None,None,'main','c_Ke']
    dataSourceId_cond5='c_P_i'
    exp5=[dataSourceId_cond5,'c_P_i',None,None,None,'main','c_P_i']
    dataSourceId_cond6='c_MgATP'
    exp6=[dataSourceId_cond6,'c_MgATP',None,None,None,'main','c_MgATP']
    dataSourceId_cond7='c_MgADP'
    exp7=[dataSourceId_cond7,'c_MgADP',None,None,None,'main','c_MgADP']
    dataSourceId_cond8='T'
    exp8=[dataSourceId_cond8,'T',None,None,None,'main','T']
    dataSourceId_cond9='q_mem'
    exp9=[dataSourceId_cond9,'q_mem',None,None,None,'main','q_mem']
    dataSourceId_cond10='pH'
    exp10=[dataSourceId_cond10,'pH',None,None,None,'main','pH']
    
    # Add the experimental conditions to the list. If no experimental condition is needed, keep the list empty
    exps=[exp1,exp2,exp3,exp4,exp5,exp6,exp7,exp8,exp9,exp10]
    # experimentalConditions=[(fileId,dataSourceId)], to map the data source file and the data source, can be empty if no experimental condition is needed
    experimentalConditions_map = [(fileId_observable,dataSourceId_cond),(fileId_observable,dataSourceId_cond2),(fileId_observable,dataSourceId_cond3),(fileId_observable,dataSourceId_cond4),(fileId_observable,dataSourceId_cond5),
                                  (fileId_observable,dataSourceId_cond6),(fileId_observable,dataSourceId_cond7),(fileId_observable,dataSourceId_cond8),(fileId_observable,dataSourceId_cond9),(fileId_observable,dataSourceId_cond10)
                                  ]
    experimentalConditions_map2 = [(fileId_observable2,dataSourceId_cond),(fileId_observable2,dataSourceId_cond2),(fileId_observable2,dataSourceId_cond3),(fileId_observable2,dataSourceId_cond4),(fileId_observable2,dataSourceId_cond5),
                                   (fileId_observable2,dataSourceId_cond6),(fileId_observable2,dataSourceId_cond7),(fileId_observable2,dataSourceId_cond8),(fileId_observable2,dataSourceId_cond9),(fileId_observable2,dataSourceId_cond10)
                                    ]
    experimentalConditions_map3 = [(fileId_observable3,dataSourceId_cond),(fileId_observable3,dataSourceId_cond2),(fileId_observable3,dataSourceId_cond3),(fileId_observable3,dataSourceId_cond4),(fileId_observable3,dataSourceId_cond5),
                                   (fileId_observable3,dataSourceId_cond6),(fileId_observable3,dataSourceId_cond7),(fileId_observable3,dataSourceId_cond8),(fileId_observable3,dataSourceId_cond9),(fileId_observable3,dataSourceId_cond10)
                                    ]
    experimentalConditions_map4 = [(fileId_observable4,dataSourceId_cond),(fileId_observable4,dataSourceId_cond2),(fileId_observable4,dataSourceId_cond3),(fileId_observable4,dataSourceId_cond4),(fileId_observable4,dataSourceId_cond5),
                                   (fileId_observable4,dataSourceId_cond6),(fileId_observable4,dataSourceId_cond7),(fileId_observable4,dataSourceId_cond8),(fileId_observable4,dataSourceId_cond9),(fileId_observable4,dataSourceId_cond10)
                                    ]
    for fid in fileId_observables:
        for exp in exps:
            dataSourceId=exp[0]
            column_name=exp[1]
            startIndex=exp[2]
            endIndex=exp[3]
            index_value=exp[4]
            component=exp[5]
            name=exp[6]
            experimentData_files[fid]['experimentalConditions'][dataSourceId]={'column_name':column_name,'startIndex':startIndex,'endIndex':endIndex,'index_value':index_value,'component':component,'name':name}

    # ******************** This is to specify the fitting experiments ********************
    # fitExperiments
    # format: [fitId, type, model_variance, algorithm, experimentalConditions_map, observables_map,time_map]

    # time=(fileId,dataSourceId) to map the data source file and the data source
    fitId_1='fit1' # fitId: the id for the fit experiment
    fitting_type='steadyState' #  the type of the fit experiment, which could be 'steadyState', or 'timeCourse'
    # model_variance: the model variance, default is ''
    # dict_algorithm_sim: the simulation algorithm information for the fit experiment
    fit1=[fitId_1,fitting_type, '',  dict_algorithm_sim, experimentalConditions_map, observables_map,time_map ]
    fitId_2='fit2' # fitId: the id for the fit experiment
    fitting_type='steadyState' #  the type of the fit experiment, which could be 'steadyState', or 'timeCourse'
    fit2=[fitId_2,fitting_type, '',  dict_algorithm_sim, experimentalConditions_map2, observables_map2,time_map ]
    fitId_3='fit3' # fitId: the id for the fit experiment
    fitting_type='steadyState' #  the type of the fit experiment, which could be 'steadyState', or 'timeCourse'
    fit3=[fitId_3,fitting_type, '',  dict_algorithm_sim, experimentalConditions_map3, observables_map3,time_map ]
    fitId_4='fit4' # fitId: the id for the fit experiment
    fitting_type='steadyState' #  the type of the fit experiment, which could be 'steadyState', or 'timeCourse'
    fit4=[fitId_4,fitting_type, '',  dict_algorithm_sim, experimentalConditions_map4, observables_map4,time_map ]


    # Add the fit experiments to the list
    fits=[fit1,fit2,fit3,fit4]

    # ******************** This is to specify the adjustable parameters for the fitting experiments ********************
    # adjustableParameters
    # format: [parameterId, component, name, lowerBound, upperBound, initialValue, scale, experimentReferences]
    #experimentReferences: list of fitId

    parameterId_1='K_1'
    adjustable1=[parameterId_1,'main','K_1',1,1e4,4000,'linear',[fitId_1,fitId_2,fitId_3,fitId_4]]
    parameterId_2='K_2'
    adjustable2=[parameterId_2,'main','K_2',1,1e3,10,'linear',[fitId_1,fitId_2,fitId_3,fitId_4]]
    parameterId_3='K_3'
    adjustable3=[parameterId_3,'main','K_3',1,1e8,1000,'linear',[fitId_1,fitId_2,fitId_3,fitId_4]]
    parameterId_4='K_4'
    adjustable4=[parameterId_4,'main','K_4',1,1e3,10,'linear',[fitId_1,fitId_2,fitId_3,fitId_4]]
    parameterId_5='kappa_1'
    adjustable5=[parameterId_5,'main','kappa_1',1,1e4,1,'linear',[fitId_1,fitId_2,fitId_3,fitId_4]]
    parameterId_6='kappa_2'
    adjustable6=[parameterId_6,'main','kappa_2',1e-3,100,1,'linear',[fitId_1,fitId_2,fitId_3,fitId_4]]
    parameterId_7='kappa_3'
    adjustable7=[parameterId_7,'main','kappa_3',1e2,1e6,2e5,'linear',[fitId_1,fitId_2,fitId_3,fitId_4]]
    parameterId_8='kappa_4'
    adjustable8=[parameterId_8,'main','kappa_4',1e-3,100,1,'linear',[fitId_1,fitId_2,fitId_3,fitId_4]]
    adjustables=[adjustable1,adjustable2,adjustable3,adjustable4,adjustable5,adjustable6,adjustable7,adjustable8]

    # ********** No need to modify the following **********

    fitExperiments={}
    for fit in fits:
        fitId=fit[0]
        type=fit[1]
        model_variance=fit[2]
        algorithm=fit[3]
        experimentalConditions=fit[4]
        observables=fit[5]
        if len(fit)==7 and type=='timeCourse':
            time=fit[6]
            fitExperiments[fitId]={'type':type,'algorithm':algorithm,'experimentalConditions':experimentalConditions,'observables':observables,'time':time}
        else:
            fitExperiments[fitId]={'type':type,'algorithm':algorithm,'experimentalConditions':experimentalConditions,'observables':observables}
        if model_variance!='':
            fitExperiments[fitId]['name']=model_variance

    adjustableParameters={}
    for adjustable in adjustables:
        parameterId=adjustable[0]
        component=adjustable[1]
        name=adjustable[2]
        lowerBound=adjustable[3]
        upperBound=adjustable[4]
        initialValue=adjustable[5]
        scale=adjustable[6]
        experimentReferences=adjustable[7]
        adjustableParameters[parameterId]={'component':component,'name':name,'lowerBound':lowerBound,'upperBound':upperBound,'initialValue':initialValue,'scale':scale,'experimentReferences':experimentReferences}

    try:            
        add_peTask2dict(dict_sedDocument, model_names, model_sources,changes,experimentData_files, adjustableParameters,fitExperiments,dict_algorithm_opt )
    except ValueError as err:
        print(err)
        exit()

    # You can repeat the above steps to add more tasks with DIFFERENT model names.

    # ********** The following is to create the sedml file, no need to modify **********

    try:
        doc=create_sedDocment(dict_sedDocument)
    except ValueError as err:
        print(err)
        exit()
    write_sedml(doc,full_path)
    print(validate_sedml(full_path))


pe_task()