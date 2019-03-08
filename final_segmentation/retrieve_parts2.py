import numpy as np
from open3d import *
from itertools import combinations
pcd=read_point_cloud("12.ply")
arr=np.asarray(pcd.points)
pcd_tree=KDTreeFlann(pcd)
with open('sss.obj','w') as f:
	for i in arr:
		f.write('v {} {} {}\n'.format(i[0],i[1],i[2]))
	for i in range(len(arr)):
		[k,idx,_]=pcd_tree.search_knn_vector_3d(pcd.points[i],10)
		idx=np.asarray(idx)
		list1=idx[1:].tolist()
		comb=combinations(list1,2)
		for i in list(comb):
			print(i)
			f.write('f {} {} {}\n'.format(int(idx[0])+1,i[0]+1,i[1]+1))	
		















