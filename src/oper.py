import sys,os,time,commands  
from operator import itemgetter
import operator
import jsonconf

#define
FILENUM = 1
OTHERSLANGUAGEINDEX = 9
OTHERSLANGUAGETYPE = 'others'

#TODO:Identify file-type  
def ftype(path):
	index = path.rfind('.')
	return path[index+1:]
def root_dir():
	root = os.getcwd()
	rtemp = root.rfind('/src')
	return root[:rtemp]

def free_result(path):
	root = os.getcwd()
	root = root_dir()
	cmd = 'rm '+ root +'/conf/topo.txt'
	try:
		output = commands.getoutput(cmd)
	except:
		print 'Init topo-file ERROR'
		exit(1)

def define_result(path, ftype, lines, note, null, date, size):
	root = root_dir()
	try:
		f = open(root+'/conf/topo.txt','a+')
		data = path+' '+ftype+' '+str(lines)+' '+str(note)+' '+str(null)+' '+str(date)+' '+str(size)+'\n'
		f.write(data)
	except:
		print "Write Topo ERROR"
		exit(0)
	f.close()

def read_result(path):
	res = []
	index = 0
	for line in file(path):
		data = {}
		line=line.strip()
		if not line:
			continue
		else:
			line = line.split(' ')
			data['index'] = index
			data['path'] = line[0]
			data['ftype'] = line[1]
			data['lines'] = long(line[2])
			data['note'] = long(line[3])
			data['null'] = long(line[4])
			data['date'] = float(line[5])
			data['size'] = long(line[6])

			res.append(data)
		index = index + 1
	return res

def ftype_map(ftype):
	types = {'cpp':0, 'c':1, 'php':2, 'py':3, 'go':4, 'js':5, 'sh':6, 'java':7, 'html':8}
	if types.has_key(ftype):
		return types[ftype]
	else:
		return OTHERSLANGUAGEINDEX
def ftype_maptype(ftype):
	types = {'cpp':'cpp', 'c':'c', 'php':'php', 'py':'py', 'go':'go', 'js':'js', 'sh':'sh', 'java':'java', 'html':'html'}
	if types.has_key(ftype):
		return types[ftype]
	else:
		return OTHERSLANGUAGETYPE

def code_rewrite(attribute, data_add):
	return attribute + data_add

def date_rewrite(attribute, attr_date, date, data_add):
	date_map = {'date-y':31536000, 'date-m':2592000, 'date-w':604800, 'date-d':86400}
	if time.time() - date >= date_map[attr_date]:
		attribute = attribute + data_add
	return attribute

def json_rewrite(path, ftype, lines, note, null, date):
	data = jsonconf.read_json(path)
	#TODO:rewrite data
	index = ftype_map(ftype)

	data['code'][0][ftype_maptype(ftype)][0]['lines'] = code_rewrite(data['code'][0][ftype_maptype(ftype)][0]['lines'], lines)

	data['code'][0][ftype_maptype(ftype)][0]['note'] = code_rewrite(data['code'][0][ftype_maptype(ftype)][0]['note'], note)

	data['code'][0][ftype_maptype(ftype)][0]['null'] = code_rewrite(data['code'][0][ftype_maptype(ftype)][0]['null'], null)

	data['code'][0][ftype_maptype(ftype)][0]['file'] = code_rewrite(data['code'][0][ftype_maptype(ftype)][0]['file'], FILENUM)


	data['date'][0]['date-y'][index]['file'] = date_rewrite(data['date'][0]['date-y'][index]['file'], 'date-y', date, FILENUM)
	data['date'][0]['date-y'][index]['lines'] = date_rewrite(data['date'][0]['date-y'][index]['lines'], 'date-y', date, lines)

	data['date'][0]['date-m'][index]['file'] = date_rewrite(data['date'][0]['date-m'][index]['file'], 'date-m', date, FILENUM)
	data['date'][0]['date-m'][index]['lines'] = date_rewrite(data['date'][0]['date-m'][index]['lines'], 'date-m', date, lines)

	data['date'][0]['date-w'][index]['file'] = date_rewrite(data['date'][0]['date-w'][index]['file'], 'date-w', date, FILENUM)
	data['date'][0]['date-w'][index]['lines'] = date_rewrite(data['date'][0]['date-w'][index]['lines'], 'date-w', date, lines)

	data['date'][0]['date-d'][index]['file'] = date_rewrite(data['date'][0]['date-d'][index]['file'], 'date-d', date, FILENUM)
	data['date'][0]['date-d'][index]['lines'] = date_rewrite(data['date'][0]['date-d'][index]['lines'], 'date-d', date, lines)

	jsonconf.write_json(path, data)
