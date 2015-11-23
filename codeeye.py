import sys,os,time,commands  
from optparse import OptionParser

type_note = {'cpp':'/*//', 'c':'/*//', 'py':'#', 'php':'#/*//', 'js':'/*//', 'java':'/*//', 'sh':'#', 'go':'/*//', 'html':'<!-->'}

def free_topo(path):
	root = os.getcwd()
	cmd = 'rm '+ root +'/topo.txt'
	try:
		output = commands.getoutput(cmd)
	except:
		print 'Init topo-file ERROR'
		exit(1)

def define_topo(path, ftype, lines, note, null, date, size):
	root = os.getcwd()
	try:
		f = open(root+'/topo.txt','a+')
		data = path+' '+ftype+' '+str(lines)+' '+str(note)+' '+str(null)+' '+str(date)+' '+str(size)+'\n'
		f.write(data)
	except:
		print "Write Topo ERROR"
		exit(0)
	f.close()

#TODO:Identify file-type  
def file_type(path):
	index = path.rfind('.')
	return path[index+1:]

#TODO:Count the lines
def line_count():
	pass

#TODO:Identify file
def identify_file(f_path):  
	lines = null = note = size =0
	# _,file_type = f_path.split('.')

	file_type = file_type(f_path)
	date = os.stat(f_path).st_mtime
	size = os.path.getsize(f_path)

	#sort file by type
	for line in file(f_path):
		line = line.split()
		if not line:
			null = null + 1
		else:
			lines = lines + 1
	define_topo(f_path, file_type, lines, note, null, date, size)


#Walk all files
def walk_files(path):
	for root, dirs, files in os.walk(path):
		#files
		print root
		if root.find('.git') >= 0:
			print 'Hide or invalid file'
			continue
		for c_file in files:
			f_path =  root + '/' + c_file;
			identify_file(f_path)
		
if(__name__=='__main__'):  
	usage = "%prog [options] [netcard name]"
	desc ="Manage Network"
	parser = OptionParser(usage=usage, description=desc)
	# parser.add_option("-i", "--info", dest="info", action="store_true", help="Get netcard info")
	parser.add_option("-p", "--path", dest="path", action="store", help="File path")
	# parser.add_option("-f", "--fresh", dest="fresh", help="Fresh DNS config ")

	(options, args) = parser.parse_args()
	# get path
	if not options.path is None:
		rpath = options.path
	else:
		rpath = os.getcwd()
	print rpath
	free_topo(rpath)
	walk_files(rpath)


