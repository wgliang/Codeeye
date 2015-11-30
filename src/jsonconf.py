import json

#Read json
def read_json(path):
	f = file(path)
	python_object = json.load(f)
	return python_object

#Write json
def write_json(path, python_object):
	with open(path,'w') as f:
		json_object = json.dump(python_object, f)

def init_json(path):
	data = read_json(path)
	


