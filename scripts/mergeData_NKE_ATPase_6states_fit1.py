import os
import sys
import pandas as pd
# Get the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '../dataPlot/'))
from manData import combine_csv_files
path_=os.path.join(current_dir, '../data/')

model_name='NKE_pump_BG_6states_fit1'

csv_files = []
model_ids_=['_v_m120', '_v_m100', '_v_m50', '_v_0', '_v_50', '_v_60']
for model_id_ in model_ids_:
    sed_model_id = model_name+model_id_
    csv_files.append(path_+'report_task_'+f'{sed_model_id}'+'.csv')

ss_csv = path_+f'{model_name}_volt_ss.csv'
if os.path.exists(ss_csv):
    os.remove(ss_csv)
with open(ss_csv, 'w') as file:
    for csv_file in csv_files:
        with open(csv_file, 'r') as f:
            if csv_file == csv_files[0]:
                file.write(f.read())
            else:
                f.readline()
                file.write(f.read())

csv_files = []
model_ids_=['_Nai_0', '_Nai_2', '_Nai_5', '_Nai_10', '_Nai_20', '_Nai_40', '_Nai_60', '_Nai_80']
for model_id_ in model_ids_:
    sed_model_id = model_name+model_id_
    csv_files.append(path_+'report_task_'+f'{sed_model_id}'+'.csv')

ss_csv = path_+f'{model_name}_Nai_ss.csv'
if os.path.exists(ss_csv):
    os.remove(ss_csv)
with open(ss_csv, 'w') as file:
    for csv_file in csv_files:
        with open(csv_file, 'r') as f:
            if csv_file == csv_files[0]:
                file.write(f.read())
            else:
                f.readline()
                file.write(f.read())

csv_files = []
model_ids_=['_Ke_0', '_Ke_05', '_Ke_1', '_Ke_2', '_Ke_4', '_Ke_6', '_Ke_8', '_Ke_10']
for model_id_ in model_ids_:
    sed_model_id = model_name+model_id_
    csv_files.append(path_+'report_task_'+f'{sed_model_id}'+'.csv')

ss_csv = path_+f'{model_name}_Ke_ss.csv'
if os.path.exists(ss_csv):
    os.remove(ss_csv)
with open(ss_csv, 'w') as file:
    for csv_file in csv_files:
        with open(csv_file, 'r') as f:
            if csv_file == csv_files[0]:
                file.write(f.read())
            else:
                f.readline()
                file.write(f.read())

csv_files = []
model_ids_=['_ATP_0', '_ATP_005', '_ATP_01', '_ATP_02', '_ATP_04', '_ATP_06']
for model_id_ in model_ids_:
    sed_model_id = model_name+model_id_
    csv_files.append(path_+'report_task_'+f'{sed_model_id}'+'.csv')

ss_csv = path_+f'{model_name}_ATP_ss.csv'
if os.path.exists(ss_csv):
    os.remove(ss_csv)
with open(ss_csv, 'w') as file:
    for csv_file in csv_files:
        with open(csv_file, 'r') as f:
            if csv_file == csv_files[0]:
                file.write(f.read())
            else:
                f.readline()
                file.write(f.read())

ss_csv_file_volt=path_+'New_Terkildsen_NaK_BG_Fig5_Data.csv'

df_ss_volt = pd.read_csv(ss_csv_file_volt)
df_ss_new = pd.DataFrame()
df_ss_new['u_e'] = df_ss_volt['environment | V_mem (volt)']*1000
df_ss_new['v_1'] = df_ss_volt['environment | v_R1 (fmol_per_sec)']
df_ss_new.to_csv(path_+'Terkildsen_NaK_BG_Fig5_Data.csv', index=False)