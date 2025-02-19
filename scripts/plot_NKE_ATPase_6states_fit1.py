import os
import sys
# Get the directory containing the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '../dataPlot/'))
from dataPlot import plot_line2D
path_=os.path.join(current_dir, '../data/')
save_fig = {'save_fig': True, 'fig_format': 'tif', 'file_path': path_, 'filename': 'NKE_pump_BG_6states_fit1'}
filename_volt = path_+'Terkildsen_NaK_BG_Fig5_Data.csv'
filename_Nai = path_+'Terkildsen_NaK_kinetic_Fig3a_Data.csv'
filename_Ke = path_+'Terkildsen_NaK_kinetic_Fig3b_Data.csv'
filename_ATP = path_+'Terkildsen_NaK_kinetic_Fig3c_Data.csv'
filename_BG_volt = path_+'NKE_pump_BG_6states_fit1_volt_ss.csv'
filename_BG_Nai = path_+'NKE_pump_BG_6states_fit1_Nai_ss.csv'
filename_BG_Ke = path_+'NKE_pump_BG_6states_fit1_Ke_ss.csv'
filename_BG_ATP = path_+'NKE_pump_BG_6states_fit1_ATP_ss.csv'


subtitle_kwargs={}
fig_cfg = {'num_rows': 2, 'num_cols': 2, 'width':8, 'height':6, 'fig_title': None, 'title_y': 1, 'fontsize': 8, 
           'left': 0.1, 'bottom': 0.15, 'right': 0.9, 'top': 0.95, 'wspace': 0.2, 'hspace': 0.4}|save_fig
#fig, axs= subplots_ajdust(fig_cfg, **subtitle_kwargs)

plot_cfg = {}
line_cfg = {}

line_cfg[1] = { 'xdata': (filename_volt,'u_e'), 'ydata':(filename_volt,'v_1'),
                'color': 'k', 'linestyle': '-',  'label': '15 state model'}
line_cfg[2] = { 'xdata': (filename_BG_volt,'V_mem'), 'ydata':(filename_BG_volt,'v_R1'),
                'color': 'r', 'linestyle': '--',  'label': '6 state model'}
line_cfg[3] = { 'xdata': (filename_Nai,'environment | Nai (mM)'), 'ydata':(filename_Nai,'environment | v_cyc_nak (per_second)'),
                'color': 'k', 'linestyle': '-',  'label': '15 state ss model'}
line_cfg[4] = { 'xdata': (filename_BG_Nai,'c_Nai'), 'ydata':(filename_BG_Nai,'v_R1'),
                'color': 'r', 'linestyle': '--',  'label': '6 state model'}
line_cfg[5] = { 'xdata': (filename_Ke,'environment | Ke (mM)'), 'ydata':(filename_Ke,'environment | v_cyc_nak (per_second)'),
                'color': 'k', 'linestyle': '-',  'label': '15 state ss model'}
line_cfg[6] = { 'xdata': (filename_BG_Ke,'c_Ke'), 'ydata':(filename_BG_Ke,'v_R1'),
                'color': 'r', 'linestyle': '--',  'label': '6 state model'}
line_cfg[7] = { 'xdata': (filename_ATP,'environment | MgATP (mM)'), 'ydata':(filename_ATP,'environment | v_cyc_nak (per_second)'),
                'color': 'k', 'linestyle': '-',  'label': '15 state ss model'}
line_cfg[8] = { 'xdata': (filename_BG_ATP,'c_MgATP'), 'ydata':(filename_BG_ATP,'v_R1'),
                'color': 'r', 'linestyle': '--',  'label': '6 state model'}
line_cfg[9] = { 'xdata': (filename_BG_volt,'V_mem'), 'ydata':(filename_BG_volt,'v_R3'),
                'color': 'b', 'linestyle': '--',  'label': '6 state ss model'}
line_cfg[10] = { 'xdata': (filename_BG_Nai,'c_Nai'), 'ydata':(filename_BG_Nai,'v_R3'),
                'color': 'b', 'linestyle': '--',  'label': '6 state ss model'}
line_cfg[11] = { 'xdata': (filename_BG_Ke,'c_Ke'), 'ydata':(filename_BG_Ke,'v_R3'),
                'color': 'b', 'linestyle': '--',  'label': '6 state ss model'}
line_cfg[12] = { 'xdata': (filename_BG_ATP,'c_MgATP'), 'ydata':(filename_BG_ATP,'v_R3'),
                'color': 'b', 'linestyle': '--',  'label': '6 state ss model'}


plot_cfg[1] = {'ylabel': 'cycle rate', 'xlabel': 'potential (mV)','show_grid': 'both', 'grid_axis': 'both',  'title_y': -0.3,
                'line': [1,2], 'legend': [1,2]}
plot_cfg[2] = {'ylabel': 'cycle rate', 'xlabel': 'Na_i (mM)','show_grid': 'both', 'grid_axis': 'both',   'title_y': -0.3,
                'line': [3,4], 'legend': [3,4]}
plot_cfg[3] = {'ylabel': 'cycle rate', 'xlabel': 'K_e (mM)','show_grid': 'both', 'grid_axis': 'both',  'title_y': -0.3,
                'line': [5,6], 'legend': [5,6]}
plot_cfg[4] = {'ylabel': 'cycle rate', 'xlabel': 'ATP (mM)','show_grid': 'both', 'grid_axis': 'both', 'title_y': -0.3,
                'line': [7,8], 'legend': [7,8]}


plot_line2D(fig_cfg, plot_cfg, line_cfg)