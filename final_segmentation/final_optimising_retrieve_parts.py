import trimesh,math
import numpy as np
from create_parts_obj import create_obj
from read_vertices_faces_obj import retrieve_vertices_faces
import os

obj_path='/home/administrator/Desktop/3d_video_avatar/SMPL_python_v.1.0.0/smpl/final_segmentation/input/punjal_new.obj'
[v,faces]=retrieve_vertices_faces(obj_path)
if not os.path.exists('results'):
	os.mkdir('results')

pant_points=np.array([np.array(c) for c in v if c[1]<=-0.25])
pant_faces=np.array([np.array(face) for face in faces if (v[face[0]-1][1]<=-0.25)])
create_obj('results/pant_segment.obj',v,pant_faces)

waist_points=np.array([np.array(c) for c in v if c[1]>-0.25 and c[1]<-0.1])
waist_faces=np.array([np.array(face) for face in faces if (v[face[0]-1][1]>-0.25) and (v[face[0]-1][1]<-0.1) ])
create_obj('results/waist_segment.obj',v,waist_faces)


chest_points=np.array([np.array(c) for c in v if  c[1]>=0.05 and c[1]<0.2 and c[0]>=-0.2 and c[0]<=0.2])
chest_faces=np.array([np.array(face) for face in faces if (v[face[0]-1][1]>=0.05) and (v[face[0]-1][1]<0.2) and (v[face[0]-1][0]>=-0.2) and(v[face[0]-1][0]<=0.2)])
create_obj('results/chest_segment.obj',v,chest_faces)

right_hand_points=np.array([np.array(c) for c in v if c[0]<=-0.2 ])
right_hand_faces=np.array([np.array(face) for face in faces if (v[face[0]-1][0]<=-0.2)])
create_obj('results/right_hand_segment.obj',v,right_hand_faces)


left_hand_points=np.array([np.array(c) for c in v if c[0]>=0.2])
left_hand_faces=np.array([np.array(face) for face in faces if (v[face[0]-1][0]>=0.2) ])
create_obj('results/left_hand_segment.obj',v,left_hand_faces)


neck_points=np.array([np.array(c) for c in v if  c[1]>=0.3 and c[1]<0.35])
neck_faces=np.array([np.array(face) for face in faces if (v[face[0]-1][1]>0.3) and (v[face[0]-1][1]<0.35) ])
create_obj('results/neck_segment.obj',v,neck_faces)


face_points=np.array([np.array(c) for c in v if c[1]>=0.35])
face_faces=np.array([np.array(face) for face in faces if (v[face[0]-1][1]>=0.35) ])
create_obj('results/face_segment.obj',v,face_faces)

'''
pant_size=(max(pant_points[:,1])-min(pant_points[:,1]))*100  #in centimeters
pant_size_in_inches=pant_size/2.54  #in inches
print("pant_size in centimeters:",pant_size)
waist_size=(math.pi*(max(waist_points[:,0])-min(waist_points[:,0]))*(max(waist_points[:,2])-min(waist_points[:,2]))/4)*1000
waist_size_in_inches=waist_size/2.54
print("waist in inches:",waist_size_in_inches)
chest_size=(math.pi*(max(chest_points[:,0])-min(chest_points[:,0]))*(max(chest_points[:,2])-min(chest_points[:,2]))/4)*1000
chest_size_in_inches=waist_size/2.54
print("chest in inches:",chest_size_in_inches)
'''

