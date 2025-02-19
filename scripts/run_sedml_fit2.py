import os
import sys
# Get the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
# Append the 'sedCellMLPy' directory to the system path
sys.path.append(os.path.join(current_dir, '../sedCellMLPy/'))
from sedCollector import read_sedml
from sedExecutor import exec_sed_doc
from pathlib import Path

path_='../models/'
working_dir = os.path.join(current_dir, path_)
sedFiles=['NKE_pump_BG_6states_fit2_Nai_V2.sedml','NKE_pump_BG_6states_fit2_Ke_V2.sedml','NKE_pump_BG_6states_fit2_ATP_V2.sedml','NKE_pump_BG_6states_fit2_volt_V2.sedml']
ss_time={'fit1':80,'fit2':80,'fit3':80,'fit4':80}

for sedFile in sedFiles:
    full_path=os.path.join(current_dir, path_,sedFile)
    doc=read_sedml(full_path)
    exec_sed_doc(doc, working_dir, working_dir, rel_out_path='../data/', external_variables_info={},
                  external_variables_values=[],ss_time=ss_time,cost_type='AE')