
def create_obj(filename,v,faces):
	with open(filename,'w') as f:
		for vrt in v:
			f.write('v {} {} {}\n'.format(vrt[0],vrt[1],vrt[2]))
		for face in faces:
			f.write('f {} {} {}\n'.format(face[0],face[1],face[2]))
