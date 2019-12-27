import sys
sys.path.append('..')

import config
from lib.io_chem import io
from lib.basic_operations import physics
from source import shift_origin
from helper_functions import createSystem,getRingDf,getTrackDf


def shiftOrigin():
  '''
  frame1_no=0
  frame2_no=10000
  file=open(config.test_file_path,'r')
  '''
  frame1_no=0
  frame2_no=1
  file=open('test_systems/ring_track_two_frames.xyz','r')

  frame1_initial_cords_df=io.readFileMd(file,frame1_no,frame_no_pos=config.frame_no_pos)
  frame2_initial_cords_df=io.readFileMd(file,frame2_no,frame_no_pos=config.frame_no_pos)
  part='whole'
  _createSystem(frame1_initial_cords_df,frame2_initial_cords_df,'output/shift_origin_initial.xyz',part=part)
  frame1_final_cords_df,frame2_final_cords_df=shift_origin.shiftOrigin(frame1_initial_cords_df,frame2_initial_cords_df)
  _createSystem(frame1_final_cords_df,frame2_final_cords_df,'output/shift_origin_final.xyz',part=part)

  ring_atom_list=range(config.ring_start_atom_no,config.ring_end_atom_no+1)
  frame1_ring_com=physics.getCom(frame1_final_cords_df,atom_list=ring_atom_list)
  frame2_ring_com=physics.getCom(frame2_final_cords_df,atom_list=ring_atom_list)
  print(frame1_ring_com)
  print(frame2_ring_com)


def _createSystem(frame1_cords_df,frame2_cords_df,output_file_path,part='ring',atom_list=None):
  if part=='ring':
    print('ring')
    frame1_part_cords_df=getRingDf(frame1_cords_df)
    frame2_part_cords_df=getRingDf(frame2_cords_df)
  elif part=='track':
    print('track')
    frame1_part_cords_df=getTrackDf(frame1_cords_df)
    frame2_part_cords_df=getTrackDf(frame2_cords_df)
  elif part=='whole':
    frame1_part_cords_df=frame1_cords_df
    frame2_part_cords_df=frame2_cords_df
  else:
    assert len(atom_list)!=0,'atoms_list should not be empty' 
  ring_atom_list=range(config.ring_start_atom_no,config.ring_end_atom_no+1)
  frame1_ring_com=physics.getCom(frame1_cords_df,atom_list=ring_atom_list)
  frame2_ring_com=physics.getCom(frame2_cords_df,atom_list=ring_atom_list)
  cords_list=[]
  atom_list=[]
  cords_list.extend(frame1_part_cords_df[['x','y','z']].values)
  cords_list.extend(frame2_part_cords_df[['x','y','z']].values)
  cords_list.extend([frame1_ring_com,frame2_ring_com])
  atom_list.extend(frame1_part_cords_df['atom'].values)
  atom_list.extend(frame2_part_cords_df['atom'].values)
  atom_list.extend(['b','b'])
  createSystem(cords_list,atom_list,output_file_path,add_axes=True)


shiftOrigin()