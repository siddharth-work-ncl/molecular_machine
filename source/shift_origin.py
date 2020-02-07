from lib.basic_operations import physics,vector
import config


def _shiftOrigin(cords,origin):
  new_cords=cords.copy()
  new_cords['x']=new_cords['x']-origin[0]
  new_cords['y']=new_cords['y']-origin[1]
  new_cords['z']=new_cords['z']-origin[2]
  return new_cords

def isZero(l):
  for i in l:
    if round(i,6)!=0:
      return False
  return True

def shiftOrigin(frame1_cords,frame2_cords,process='rotation'): 
  trans_axis=[0.0,0.0,0.0] 
  ref_axis_atom1_cords=frame1_cords[frame1_cords['atom_no']==config.ref_axis_atom1_no][['x','y','z']].values[0]
  ref_axis_atom2_cords=frame1_cords[frame1_cords['atom_no']==config.ref_axis_atom2_no][['x','y','z']].values[0]
  trans_axis[0]=ref_axis_atom2_cords[0]-ref_axis_atom1_cords[0]
  trans_axis[1]=ref_axis_atom2_cords[1]-ref_axis_atom1_cords[1]
  trans_axis[2]=ref_axis_atom2_cords[2]-ref_axis_atom1_cords[2]
  if process=='rotation':
    cog1=physics.getCog(frame1_cords,atom_list=config.ring_atom_no_list)
    cog2=physics.getCog(frame2_cords,atom_list=config.ring_atom_no_list)
    new_frame1_cords=_shiftOrigin(frame1_cords,cog1)
    new_frame2_cords=_shiftOrigin(frame2_cords,cog2)
  elif process=='translation':
    com1=physics.getCom(frame1_cords,atom_list=config.ring_atom_no_list)
    com2=physics.getCom(frame2_cords,atom_list=config.ring_atom_no_list)
    new_frame1_cords=_shiftOrigin(frame1_cords,com1)
    new_frame2_cords=_shiftOrigin(frame2_cords,com1)
  if config.axis=='x':
    ax=[1,0,0]
  elif config.axis=='y':
    ax=[0,1,0]
  elif config.axis=='z':
    ax=[0,0,1]
  if not isZero(trans_axis):
    axis=vector.getCrossProduct(trans_axis,ax)
    theta=vector.getAngleR(trans_axis,ax)  
    new_frame1_cords=physics.rotateAlongAxis(new_frame1_cords,axis,theta)
    new_frame2_cords=physics.rotateAlongAxis(new_frame2_cords,axis,theta)
  
  whole_frame_cog=physics.getCog(new_frame1_cords) 
  if config.axis=='x':
    ref_axis=[0,1,1]
    whole_frame_cog[0]=0
  elif config.axis=='y':
    ref_axis=[1,0,1]
    whole_frame_cog[1]=0
  elif config.axis=='z':
    ref_axis=[1,1,0]
    whole_frame_cog[2]=0
  axis=vector.getCrossProduct(whole_frame_cog,ref_axis)
  theta=vector.getAngleR(whole_frame_cog,ref_axis)
  new_frame1_cords=physics.rotateAlongAxis(new_frame1_cords,axis,theta)
  new_frame2_cords=physics.rotateAlongAxis(new_frame2_cords,axis,theta)

  return (new_frame1_cords,new_frame2_cords)
