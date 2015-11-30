import sys,os,time,commands  
from operator import itemgetter
import operator
import jsonconf

labels = ['C++', 'C', 'PHP', 'Python', 'Go', 'JavaScript', 'Shell', 'Java', 'HTML']
date_map = {'date-y':31536000, 'date-m':2592000, 'date-w':604800, 'date-d':86400, 'date-h':3600}
#Global define
FILENUM = 1
OTHERSLANGUAGEINDEX = 9
OTHERSLANGUAGETYPE = 'Others'

#Get file type
def ftype(path):
	index = path.rfind('.')
	return path[index+1:]

#Get dir of root
def root_dir():
	root = os.getcwd()
	rtemp = root.rfind('/src')
	return root[:rtemp]

#Free result in topo
def free_result(path):
	root = os.getcwd()
	root = root_dir()
	cmd = 'rm '+ root +'/conf/topo.txt'
	try:
		output = commands.getoutput(cmd)
	except:
		print 'Init topo-file ERROR'
		exit(1)
	cmd = 'rm '+ root +'/conf/codeeye.json'


#Define result in topo
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

#Read result in topo
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

#Type map index
def ftype_mapindex(ftype):
	types = {'cpp':0, 'c':1, 'php':2, 'py':3, 'go':4, 'js':5, 'sh':6, 'java':7, 'html':8}
	if types.has_key(ftype):
		return types[ftype]
	else:
		return OTHERSLANGUAGEINDEX

#Type map type
def ftype_maptype(ftype):
	types = {'cpp':'C++', 'c':'C', 'php':'PHP', 'py':'Python', 'go':'Go', 'js':'JavaScrit', 'sh':'Shell', 'java':'Java', 'html':'HTML'}
	if types.has_key(ftype):
		return types[ftype]
	else:
		return OTHERSLANGUAGETYPE

#Rewrite code
def code_rewrite(attribute, data_add):
	return attribute + data_add

#Rewrite date
def date_rewrite(attribute, attr_date, date, data_add):
	if time.time() - date >= date_map[attr_date]:
		attribute = attribute + data_add
	return attribute

def date_day_identify(path):
	data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	res = read_result(path)
	for temp in res:
		duration = time.time() - temp['date']
		if duration >= 0 and duration <  date_map['date-d']:
			index = int(duration/date_map['date-h'])
			data[index] = data[index] + temp['lines']
	return data


#Init json
def json_init(path):
	data = jsonconf.read_json(path)
	#TODO:rewrite data
	for ftype in labels:
		data['code'][0][ftype][0]['lines'] = code_rewrite(0,0)

		data['code'][0][ftype][0]['note'] = code_rewrite(0,0)

		data['code'][0][ftype][0]['null'] = code_rewrite(0,0)

		data['code'][0][ftype][0]['file'] = code_rewrite(0,0)

	for index in range(0,len(labels)):
		data['date'][0]['date-y'][index]['file'] = 0
		data['date'][0]['date-y'][index]['lines'] = 0

		data['date'][0]['date-m'][index]['file'] = 0
		data['date'][0]['date-m'][index]['lines'] = 0

		data['date'][0]['date-w'][index]['file'] = 0
		data['date'][0]['date-w'][index]['lines'] = 0

		data['date'][0]['date-d'][index]['file'] = 0
		data['date'][0]['date-d'][index]['lines'] = 0

		data['date'][0]['date-h'][index]['file'] = 0
		data['date'][0]['date-h'][index]['lines'] = 0

	jsonconf.write_json(path, data)
#Rewrite json
def json_rewrite(path, ftype, lines, note, null, date):
	data = jsonconf.read_json(path)
	#TODO:rewrite data
	index = ftype_mapindex(ftype)

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

	data['date'][0]['date-h'][index]['file'] = date_rewrite(data['date'][0]['date-h'][index]['file'], 'date-h', date, FILENUM)
	data['date'][0]['date-h'][index]['lines'] = date_rewrite(data['date'][0]['date-h'][index]['lines'], 'date-h', date, lines)

	jsonconf.write_json(path, data)
