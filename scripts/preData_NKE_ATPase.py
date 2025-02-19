import os
import sys
import pandas as pd
# Get the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '../dataPlot/'))
from manData import combine_csv_files
path_=os.path.join(current_dir, '../data/')

C_m=153400
new_csv_file = path_+'Terkildsen_NaK_kinetic_Nai.csv'
ss_csv_file_Nai=path_+'Terkildsen_NaK_kinetic_Fig3a_Data.csv'

csv_files=[(ss_csv_file_Nai, 0, 0),(ss_csv_file_Nai, 11, 11), (ss_csv_file_Nai, 21, 21),(ss_csv_file_Nai, 51, 51), 
           (ss_csv_file_Nai, 101, 101), (ss_csv_file_Nai, 201, 201), (ss_csv_file_Nai, 401, 401),
           (ss_csv_file_Nai, 601, 601), (ss_csv_file_Nai, 801, 801)]
combine_csv_files(new_csv_file, csv_files)

ss_csv_file_new=path_+'Terkildsen_NaK_kinetic_Nai_cond.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['environment | t (second)'])

u_e=0
small_value=1e-6
df_ss_new['q_mem'] = [C_m*u_e for i in range(N_cond)]
df_ss_new['c_Nai'] = df_ss_old['environment | Nai (mM)']
df_ss_new['c_Nae']=[small_value for i in range(N_cond)]
df_ss_new['c_Ki']=[80 for i in range(N_cond)]
df_ss_new['c_Ke']=[15 for i in range(N_cond)]
df_ss_new['c_P_i']=[1 for i in range(N_cond)]
df_ss_new['c_MgATP']=[2 for i in range(N_cond)]
df_ss_new['c_MgADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[308 for i in range(N_cond)]
df_ss_new['pH']=[7.2 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['environment | v_cyc_nak (per_second)']
df_ss_new.to_csv(ss_csv_file_new, index=False)

new_csv_file = path_+'Terkildsen_NaK_kinetic_Ke.csv'
ss_csv_file_Nai=path_+'Terkildsen_NaK_kinetic_Fig3b_Data.csv'

csv_files=[(ss_csv_file_Nai, 0, 0),(ss_csv_file_Nai, 2, 2), (ss_csv_file_Nai, 21, 21),(ss_csv_file_Nai, 41, 41), 
           (ss_csv_file_Nai, 81, 81), (ss_csv_file_Nai, 121, 121), (ss_csv_file_Nai, 161, 161),
           (ss_csv_file_Nai, 201, 201)]
combine_csv_files(new_csv_file, csv_files)

ss_csv_file_new=path_+'Terkildsen_NaK_kinetic_Ke_cond.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['environment | t (second)'])

u_e=0
small_value=1e-6
df_ss_new['q_mem'] = [C_m*u_e for i in range(N_cond)]
df_ss_new['c_Nai'] =[50 for i in range(N_cond)]
df_ss_new['c_Nae']=[150 for i in range(N_cond)]
df_ss_new['c_Ki']=[140 for i in range(N_cond)]
df_ss_new['c_Ke']=df_ss_old['environment | Ke (mM)']
df_ss_new['c_P_i']=[0.5 for i in range(N_cond)]
df_ss_new['c_MgATP']=[10 for i in range(N_cond)]
df_ss_new['c_MgADP']=[0.02 for i in range(N_cond)]
df_ss_new['T']=[310 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['environment | v_cyc_nak (per_second)']
df_ss_new.to_csv(ss_csv_file_new, index=False)

new_csv_file = path_+'Terkildsen_NaK_kinetic_ATP.csv'
ss_csv_file_Nai=path_+'Terkildsen_NaK_kinetic_Fig3c_Data.csv'

csv_files=[(ss_csv_file_Nai, 0, 0),(ss_csv_file_Nai, 2, 2), (ss_csv_file_Nai, 6, 6),(ss_csv_file_Nai, 11, 11), 
           (ss_csv_file_Nai, 21, 21), (ss_csv_file_Nai, 41, 41), (ss_csv_file_Nai, 61, 61)]
combine_csv_files(new_csv_file, csv_files)

ss_csv_file_new=path_+'Terkildsen_NaK_kinetic_ATP_cond.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['environment | t (second)'])

u_e=0
small_value=1e-6
df_ss_new['q_mem'] = [C_m*u_e for i in range(N_cond)]
df_ss_new['c_Nai'] =[40 for i in range(N_cond)]
df_ss_new['c_Nae']=[small_value for i in range(N_cond)]
df_ss_new['c_Ki']=[small_value for i in range(N_cond)]
df_ss_new['c_Ke']=[5 for i in range(N_cond)]
df_ss_new['c_P_i']=[0.005 for i in range(N_cond)]
df_ss_new['c_MgATP']=df_ss_old['environment | MgATP (mM)']
df_ss_new['c_MgADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[297 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['environment | v_cyc_nak (per_second)']
df_ss_new.to_csv(ss_csv_file_new, index=False)

new_csv_file = path_+'Terkildsen_NaK_kinetic_volt_.csv'
ss_csv_file_Nai=path_+'New_Terkildsen_NaK_BG_Fig5_Data.csv'

csv_files=[(ss_csv_file_Nai, 0, 0),(ss_csv_file_Nai, 1, 1),(ss_csv_file_Nai, 201, 201), (ss_csv_file_Nai, 701, 701),(ss_csv_file_Nai, 1201, 1201), 
           (ss_csv_file_Nai, 1701, 1701), (ss_csv_file_Nai, 1801, 1801)]
combine_csv_files(new_csv_file, csv_files)

ss_csv_file_new=path_+'Terkildsen_NaK_kinetic_volt_cond.csv'
df_ss_new = pd.DataFrame()
df_ss_old = pd.read_csv(new_csv_file)
N_cond=len(df_ss_old['environment | t (second)'])

u_e=0
small_value=1e-6
df_ss_new['q_mem'] = df_ss_old['environment | V_mem (volt)']*C_m
df_ss_new['c_Nai'] =[50 for i in range(N_cond)]
df_ss_new['c_Nae']=[150 for i in range(N_cond)]
df_ss_new['c_Ki']=[small_value for i in range(N_cond)]
df_ss_new['c_Ke']=[5.4 for i in range(N_cond)]
df_ss_new['c_P_i']=[small_value for i in range(N_cond)]
df_ss_new['c_MgATP']=[10 for i in range(N_cond)]
df_ss_new['c_MgADP']=[small_value for i in range(N_cond)]
df_ss_new['T']=[310 for i in range(N_cond)]
df_ss_new['pH']=[7.4 for i in range(N_cond)]
df_ss_new['v_ss'] = df_ss_old['environment | v_R1 (fmol_per_sec)']
df_ss_new.to_csv(ss_csv_file_new, index=False)