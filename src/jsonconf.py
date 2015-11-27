import json

def read_json(path):
	f = file(path)
	python_object = json.load(f)
	return python_object

def write_json(path, python_object):
	with open(path,'w') as f:
		json_object = json.dump(python_object, f)


