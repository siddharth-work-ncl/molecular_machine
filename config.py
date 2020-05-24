__version__='3.0.0'

test_file_path='/home/vanka/ruchi/output_only/system3/system3_a/system3_a_md_29_12_19.xyz'

#GENERAL PARAMETERS
input_parent_dir_path="/home/vanka/ruchi/molecular_motor"
input_system_name="case_1"
input_subsystem_name="molecular_rotor.md"
input_scr_dir_name="scr"
output_parent_dir_path='output'

ring_atom_no=0
track_atom_no=30
ref_axis_atom1_no=20
ref_axis_atom2_no=37

start_frame_no=89099
end_frame_no=999999
step_size=10
frame_no_pos=2

tasks='3+0'#'3+0+4+2'

#INTERNAL PARAMETERS
track_range=2
simulation_time_step=0.5 #in femto

rotation_method='rot_part_atomic_r_t_3'
translation_method='trans_com_3'
RKE_method='energy_rot_part_atomic_r_t_3'
TKE_method='energy_trans_com_2'
axis='x'
show_plot=False

ring_atom_no_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

track_atom_no_list=[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]

code_dir_path='/home/vanka/siddharth/molecular_machines_project/molecular_machines'

'''
NOTE COMMIT(MAJOR UPDATE):
* version=3.0.0
* updating shiftOrigin,rotation and traslation methods

FUTURE TASKS:
 1. update shiftOrigin to fix sign of the rotation angle: this can potential remove the need for reference axis, it may provide correct rotation values for 'only ring and track'
 2. no need to worry about circular track, david look like straight track for most of the time-steps
 3. think about how to get correct 'only ring and track' rotation values
'''
