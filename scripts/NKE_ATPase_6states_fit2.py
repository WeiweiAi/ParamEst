import sys
import os
# Get the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Append the 'sedmlEditor' directory to the system path
sys.path.append(os.path.join(current_dir, '../sedmlEditor/'))
from sedDict import create_dict_sedDocment, add_sedTask2dict,add_peTask2dict
from sedEditor import create_sedDocment,write_sedml, validate_sedml


def BG4Statemodel_volt():
    # Convert the model to CellML 2.0 if needed
    # Convert the model to CellML 2.0 if needed
    model_name='NKE_pump_BG_6states_fit2'
    path_='../models/'
    sedFilename = model_name+'_volt_V2.sedml' 
    full_path = os.path.join(current_dir, path_, sedFilename)
    model_path ='./' 
    # ********** The following is to create a dictionary for the sedml file **********
    dict_sedDocument=create_dict_sedDocment()
    model_ids_=['_v_m120', '_v_m100', '_v_m50', '_v_0', '_v_50', '_v_60']
    small_value='1e-6'
    C_m=153400
    u_e=[-120,-100,-50,0,50,60]    
    for i in range(len(model_ids_)):
        model_id_=model_ids_[i]
        model_id = model_name+model_id_ # This is the model id in the sedml, could be different from the model file name
        # ********** The following is to add the task information to the dictionary **********

        # Note: the following is an example, you can modify it to add more tasks
        # Note: the valid sedml id should start with a letter, and only contain letters, numbers, and underscores
        # This is the model file name, assuming in the same folder with the sedml file
        model_source = model_path + model_name + '.cellml' 
        # This is to modify the model parameters if needed
        q_mem=C_m*u_e[i]/1000
        changes={'q_mem':{'component':'environment','name':'q_mem','newValue':str(q_mem)},
                 'c_Nai':{'component':'environment','name':'c_Nai','newValue':'50'},
                 'c_Nae':{'component':'environment','name':'c_Nae','newValue':'150'},
                 'c_Ki':{'component':'environment','name':'c_Ki','newValue':small_value},
                 'c_Ke':{'component':'environment','name':'c_Ke','newValue':'5.4'},
                 'c_P_i':{'component':'environment','name':'c_P_i','newValue':small_value},
                 'c_MgATP':{'component':'environment','name':'c_MgATP','newValue':'10'},
                 'c_MgADP':{'component':'environment','name':'c_MgADP','newValue':small_value},
                 'T':{'component':'environment','name':'T','newValue':'310'},
                 'pH':{'component':'environment','name':'pH','newValue':'7.4'},
                 }  
        # the format is {'id':{'component':str,'name':str,'newValue':str}}
        # Example: changes={'V_m':{'component':'environment','name':'V_m','newValue':'-0.055'}

        # This is the output of the simulation, and the key is part of the output id
        # The value is a dictionary with the following keys: 'component', 'name', 'scale'
        # component is the component name in the CellML model where the output variable is defined
        # name is the variable name of the outputs
        # scale is the scaling factor for the output variable
        outputs={'t':{'component':'environment','name':'t','scale':1},
                 'v_R1':{'component':'environment','name':'v_R1','scale':1},
                 'v_R3':{'component':'environment','name':'v_R3','scale':1},         
                 'V_mem':{'component':'environment','name':'V_mem','scale':1e3},
                 'c_Nai':{'component':'environment','name':'c_Nai','scale':1},
                 'c_Ke':{'component':'environment','name':'c_Ke','scale':1},
                 'c_MgATP':{'component':'environment','name':'c_MgATP','scale':1},
                 }
        # You can add more outputs if needed

        # The following is the simulation setting
        # This is to set the maximum step size for the simulation
        dict_algorithmParameter={'kisaoID':'KISAO:0000209', 'name':'rtol','value':'1e-9'} 
        dict_algorithmParameter2={'kisaoID':'KISAO:0000211', 'name':'atol','value':'1e-9'} 
        # You can set more algorithm parameters if needed. You can refer to get_KISAO_parameters() in src/simulator.py file to get the parameters for the specific algorithm
        # Add the algorithm parameters to listOfAlgorithmParameters
        # You can choose one of the simulation algorithms specified by KISAO_ALGORITHMS in src/simulator.py file
        dict_algorithm={'kisaoID':'KISAO:0000088','name':'LSODA','listOfAlgorithmParameters':[dict_algorithmParameter,dict_algorithmParameter2]} 
        # This is the simulation setting
        # You can choose one of the following simulation types: 'UniformTimeCourse', 'OneStep'
        simSetting={'type':'OneStep','algorithm':dict_algorithm,'step':80}
        # simSetting={'type':'OneStep','algorithm':dict_algorithm,'step':0.1}


        # The following is to add the task information to the dictionary
        add_sedTask2dict(dict_sedDocument, model_id, model_source,changes,simSetting,outputs)

        # You can repeat the above steps to add more tasks with DIFFERENT model names.

    # ********** The following is to create the sedml file, no need to modify **********
    try:
        doc=create_sedDocment(dict_sedDocument)
    except ValueError as err:
        print(err)
    write_sedml(doc,full_path)
    print(validate_sedml(full_path))

def BG4Statemodel_Nai():
    # Convert the model to CellML 2.0 if needed
    model_name='NKE_pump_BG_6states_fit2'
    path_='../models/'
    sedFilename = model_name+'_Nai_V2.sedml' 
    full_path = os.path.join(current_dir, path_, sedFilename)
    model_path ='./' 
    # ********** The following is to create a dictionary for the sedml file **********
    dict_sedDocument=create_dict_sedDocment()
    model_ids_=['_Nai_0', '_Nai_2', '_Nai_5', '_Nai_10', '_Nai_20', '_Nai_40', '_Nai_60', '_Nai_80']
    small_value='1e-6'
    Nai=['1','2','5','10','20','40','60','80']
    for i in range(len(model_ids_)):
        model_id_=model_ids_[i]
        model_id = model_name+model_id_ # This is the model id in the sedml, could be different from the model file name
        # ********** The following is to add the task information to the dictionary **********

        # Note: the following is an example, you can modify it to add more tasks
        # Note: the valid sedml id should start with a letter, and only contain letters, numbers, and underscores
        # This is the model file name, assuming in the same folder with the sedml file
        model_source = model_path + model_name + '.cellml' 
        # This is to modify the model parameters if needed
        changes={'q_mem':{'component':'environment','name':'q_mem','newValue':'0'},
                 'c_Nai':{'component':'environment','name':'c_Nai','newValue':Nai[i]},
                 'c_Nae':{'component':'environment','name':'c_Nae','newValue':small_value}, # 0
                 'c_Ki':{'component':'environment','name':'c_Ki','newValue':'80'},
                 'c_Ke':{'component':'environment','name':'c_Ke','newValue':'15'},
                 'c_P_i':{'component':'environment','name':'c_P_i','newValue':'1'},
                 'c_MgATP':{'component':'environment','name':'c_MgATP','newValue':'2'},
                 'c_MgADP':{'component':'environment','name':'c_MgADP','newValue':small_value}, # 0
                 'T':{'component':'environment','name':'T','newValue':'308'},
                 'pH':{'component':'environment','name':'pH','newValue':'7.2'},
                 }  
        # the format is {'id':{'component':str,'name':str,'newValue':str}}
        # Example: changes={'V_m':{'component':'environment','name':'V_m','newValue':'-0.055'}

        # This is the output of the simulation, and the key is part of the output id
        # The value is a dictionary with the following keys: 'component', 'name', 'scale'
        # component is the component name in the CellML model where the output variable is defined
        # name is the variable name of the outputs
        # scale is the scaling factor for the output variable
        outputs={'t':{'component':'environment','name':'t','scale':1},
                 'v_R1':{'component':'environment','name':'v_R1','scale':1},
                 'v_R3':{'component':'environment','name':'v_R3','scale':1},          
                 'V_mem':{'component':'environment','name':'V_mem','scale':1e3},
                 'c_Nai':{'component':'environment','name':'c_Nai','scale':1},
                 'c_Ke':{'component':'environment','name':'c_Ke','scale':1},
                 'c_MgATP':{'component':'environment','name':'c_MgATP','scale':1},
                 }
        # You can add more outputs if needed

        # The following is the simulation setting
        # This is to set the maximum step size for the simulation
        dict_algorithmParameter={'kisaoID':'KISAO:0000209', 'name':'rtol','value':'1e-8'} 
        dict_algorithmParameter2={'kisaoID':'KISAO:0000211', 'name':'atol','value':'1e-8'} 
        # You can set more algorithm parameters if needed. You can refer to get_KISAO_parameters() in src/simulator.py file to get the parameters for the specific algorithm
        # Add the algorithm parameters to listOfAlgorithmParameters
        # You can choose one of the simulation algorithms specified by KISAO_ALGORITHMS in src/simulator.py file
        dict_algorithm={'kisaoID':'KISAO:0000088','name':'LSODA','listOfAlgorithmParameters':[dict_algorithmParameter,dict_algorithmParameter2]} 
        # This is the simulation setting
        # You can choose one of the following simulation types: 'UniformTimeCourse', 'OneStep'
        simSetting={'type':'OneStep','algorithm':dict_algorithm,'step':80}
        # simSetting={'type':'OneStep','algorithm':dict_algorithm,'step':0.1}


        # The following is to add the task information to the dictionary
        add_sedTask2dict(dict_sedDocument, model_id, model_source,changes,simSetting,outputs)

        # You can repeat the above steps to add more tasks with DIFFERENT model names.

    # ********** The following is to create the sedml file, no need to modify **********
    try:
        doc=create_sedDocment(dict_sedDocument)
    except ValueError as err:
        print(err)
    write_sedml(doc,full_path)
    print(validate_sedml(full_path))


def BG4Statemodel_Ke():
    # Convert the model to CellML 2.0 if needed
    model_name='NKE_pump_BG_6states_fit2'
    path_='../models/'
    sedFilename = model_name+'_Ke_V2.sedml' 
    full_path = os.path.join(current_dir, path_, sedFilename)
    model_path ='./' 
    # ********** The following is to create a dictionary for the sedml file **********
    dict_sedDocument=create_dict_sedDocment()
    model_ids_=['_Ke_0', '_Ke_05', '_Ke_1', '_Ke_2', '_Ke_4', '_Ke_6', '_Ke_8', '_Ke_10']
    small_value='1e-6'
    Ke=[small_value,'0.5','1','2','4','6','8','10']
    for i in range(len(model_ids_)):
        model_id_=model_ids_[i]
        model_id = model_name+model_id_ # This is the model id in the sedml, could be different from the model file name
        # ********** The following is to add the task information to the dictionary **********

        # Note: the following is an example, you can modify it to add more tasks
        # Note: the valid sedml id should start with a letter, and only contain letters, numbers, and underscores
        # This is the model file name, assuming in the same folder with the sedml file
        model_source = model_path + model_name + '.cellml' 
        # This is to modify the model parameters if needed
        changes={'q_mem':{'component':'environment','name':'q_mem','newValue':'0'},
                 'c_Nai':{'component':'environment','name':'c_Nai','newValue':'50'},
                 'c_Nae':{'component':'environment','name':'c_Nae','newValue':'150'},
                 'c_Ki':{'component':'environment','name':'c_Ki','newValue':'140'},
                 'c_Ke':{'component':'environment','name':'c_Ke','newValue':Ke[i]},
                 'c_P_i':{'component':'environment','name':'c_P_i','newValue':'0.5'},
                 'c_MgATP':{'component':'environment','name':'c_MgATP','newValue':'10'},
                 'c_MgADP':{'component':'environment','name':'c_MgADP','newValue':'0.02'},
                 'T':{'component':'environment','name':'T','newValue':'310'},
                 'pH':{'component':'environment','name':'pH','newValue':'7.4'},
                 }  
        # the format is {'id':{'component':str,'name':str,'newValue':str}}
        # Example: changes={'V_m':{'component':'environment','name':'V_m','newValue':'-0.055'}

        # This is the output of the simulation, and the key is part of the output id
        # The value is a dictionary with the following keys: 'component', 'name', 'scale'
        # component is the component name in the CellML model where the output variable is defined
        # name is the variable name of the outputs
        # scale is the scaling factor for the output variable
        outputs={'t':{'component':'environment','name':'t','scale':1},
                 'v_R1':{'component':'environment','name':'v_R1','scale':1},
                 'v_R3':{'component':'environment','name':'v_R3','scale':1},          
                 'V_mem':{'component':'environment','name':'V_mem','scale':1e3},
                 'c_Nai':{'component':'environment','name':'c_Nai','scale':1},
                 'c_Ke':{'component':'environment','name':'c_Ke','scale':1},
                 'c_MgATP':{'component':'environment','name':'c_MgATP','scale':1},
                 }
        # You can add more outputs if needed

        # The following is the simulation setting
        # This is to set the maximum step size for the simulation
        dict_algorithmParameter={'kisaoID':'KISAO:0000209', 'name':'rtol','value':'1e-9'} 
        dict_algorithmParameter2={'kisaoID':'KISAO:0000211', 'name':'atol','value':'1e-9'} 
        # You can set more algorithm parameters if needed. You can refer to get_KISAO_parameters() in src/simulator.py file to get the parameters for the specific algorithm
        # Add the algorithm parameters to listOfAlgorithmParameters
        # You can choose one of the simulation algorithms specified by KISAO_ALGORITHMS in src/simulator.py file
        dict_algorithm={'kisaoID':'KISAO:0000088','name':'LSODA','listOfAlgorithmParameters':[dict_algorithmParameter,dict_algorithmParameter2]} 
        # This is the simulation setting
        # You can choose one of the following simulation types: 'UniformTimeCourse', 'OneStep'
        simSetting={'type':'OneStep','algorithm':dict_algorithm,'step':80}
        # simSetting={'type':'OneStep','algorithm':dict_algorithm,'step':0.1}


        # The following is to add the task information to the dictionary
        add_sedTask2dict(dict_sedDocument, model_id, model_source,changes,simSetting,outputs)

        # You can repeat the above steps to add more tasks with DIFFERENT model names.

    # ********** The following is to create the sedml file, no need to modify **********
    try:
        doc=create_sedDocment(dict_sedDocument)
    except ValueError as err:
        print(err)
    write_sedml(doc,full_path)
    print(validate_sedml(full_path))

def BG4Statemodel_ATP():
    # Convert the model to CellML 2.0 if needed
    model_name='NKE_pump_BG_6states_fit2'
    path_='../models/'
    sedFilename = model_name+'_ATP_V2.sedml' 
    full_path = os.path.join(current_dir, path_, sedFilename)
    model_path ='./' 
    # ********** The following is to create a dictionary for the sedml file **********
    dict_sedDocument=create_dict_sedDocment()
    model_ids_=['_ATP_0', '_ATP_005', '_ATP_01', '_ATP_02', '_ATP_04', '_ATP_06']
    small_value='1e-6'
    ATP=['0.01','0.05','0.1','0.2','0.4','0.6']
    for i in range(len(model_ids_)):
        model_id_=model_ids_[i]
        model_id = model_name+model_id_ # This is the model id in the sedml, could be different from the model file name
        # ********** The following is to add the task information to the dictionary **********

        # Note: the following is an example, you can modify it to add more tasks
        # Note: the valid sedml id should start with a letter, and only contain letters, numbers, and underscores
        # This is the model file name, assuming in the same folder with the sedml file
        model_source = model_path + model_name + '.cellml' 
        # This is to modify the model parameters if needed
        changes={'q_mem':{'component':'environment','name':'q_mem','newValue':'0'},
                 'c_Nai':{'component':'environment','name':'c_Nai','newValue':'40'},
                 'c_Nae':{'component':'environment','name':'c_Nae','newValue':small_value}, # 0
                 'c_Ki':{'component':'environment','name':'c_Ki','newValue':small_value}, # 0
                 'c_Ke':{'component':'environment','name':'c_Ke','newValue':'5'},
                 'c_P_i':{'component':'environment','name':'c_P_i','newValue':'0.005'}, # 0
                 'c_MgATP':{'component':'environment','name':'c_MgATP','newValue':ATP[i]},
                 'c_MgADP':{'component':'environment','name':'c_MgADP','newValue':small_value}, # 0
                 'T':{'component':'environment','name':'T','newValue':'297'},
                 'pH':{'component':'environment','name':'pH','newValue':'7.4'},
                 }  
        # the format is {'id':{'component':str,'name':str,'newValue':str}}
        # Example: changes={'V_m':{'component':'environment','name':'V_m','newValue':'-0.055'}

        # This is the output of the simulation, and the key is part of the output id
        # The value is a dictionary with the following keys: 'component', 'name', 'scale'
        # component is the component name in the CellML model where the output variable is defined
        # name is the variable name of the outputs
        # scale is the scaling factor for the output variable
        outputs={'t':{'component':'environment','name':'t','scale':1},
                 'v_R1':{'component':'environment','name':'v_R1','scale':1},
                 'v_R3':{'component':'environment','name':'v_R3','scale':1},          
                 'V_mem':{'component':'environment','name':'V_mem','scale':1e3},
                 'c_Nai':{'component':'environment','name':'c_Nai','scale':1},
                 'c_Ke':{'component':'environment','name':'c_Ke','scale':1},
                 'c_MgATP':{'component':'environment','name':'c_MgATP','scale':1},
                 }
        # You can add more outputs if needed

        # The following is the simulation setting
        # This is to set the maximum step size for the simulation
        dict_algorithmParameter={'kisaoID':'KISAO:0000209', 'name':'rtol','value':'1e-9'} 
        dict_algorithmParameter2={'kisaoID':'KISAO:0000211', 'name':'atol','value':'1e-9'} 
        # You can set more algorithm parameters if needed. You can refer to get_KISAO_parameters() in src/simulator.py file to get the parameters for the specific algorithm
        # Add the algorithm parameters to listOfAlgorithmParameters
        # You can choose one of the simulation algorithms specified by KISAO_ALGORITHMS in src/simulator.py file
        dict_algorithm={'kisaoID':'KISAO:0000088','name':'LSODA','listOfAlgorithmParameters':[dict_algorithmParameter,dict_algorithmParameter2]} 
        # This is the simulation setting
        # You can choose one of the following simulation types: 'UniformTimeCourse', 'OneStep'
        simSetting={'type':'OneStep','algorithm':dict_algorithm,'step':80}
        # simSetting={'type':'OneStep','algorithm':dict_algorithm,'step':0.1}


        # The following is to add the task information to the dictionary
        add_sedTask2dict(dict_sedDocument, model_id, model_source,changes,simSetting,outputs)

        # You can repeat the above steps to add more tasks with DIFFERENT model names.

    # ********** The following is to create the sedml file, no need to modify **********
    try:
        doc=create_sedDocment(dict_sedDocument)
    except ValueError as err:
        print(err)
    write_sedml(doc,full_path)
    print(validate_sedml(full_path))

BG4Statemodel_Nai()
BG4Statemodel_Ke()
BG4Statemodel_ATP()
BG4Statemodel_volt()