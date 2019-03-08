
def retrieve_vertices_faces(obj_path):
	verts=[]
	faces=[]
	with open(obj_path,'r') as f:
		for line in f:
			line_split=line.split(' ')
			if line_split[0]=='v':
				verts.append([float(line_split[1]),float(line_split[2]),float(line_split[3])])
			if line_split[0]=='f':
				faces.append([int(line_split[1].split('/')[0]),int(line_split[2].split('/')[0]),int(line_split[3].split('/')[0])])
	return([verts,faces])
