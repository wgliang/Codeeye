import sys,os,time,commands  
from operator import itemgetter
import operator
#TODO:Identify file-type  
def ftype(path):
	index = path.rfind('.')
	return path[index+1:]

def free_result(path):
	root = os.getcwd()
	cmd = 'rm '+ root +'/topo.txt'
	try:
		output = commands.getoutput(cmd)
	except:
		print 'Init topo-file ERROR'
		exit(1)

def define_result(path, ftype, lines, note, null, date, size):
	root = os.getcwd()
	try:
		f = open(root+'/topo.txt','a+')
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