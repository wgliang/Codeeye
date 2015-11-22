import sys,os,time  
from optparse import OptionParser

type_note = {'cpp':'/*//', 'c':'/*//', 'py':'#', 'php':'#/*//', 'js':'/*//', 'java':'/*//', 'sh':'#', 'go':'/*//', 'html':'<!-->'}

def define_topo(path, ftype, lines, note, null, date, size):
	root = os.getcwd()
	try:
		f = open(root+'/topo.txt','a+')
		data = path+' '+ftype+' '+lines+' '+note+' '+null+' '+date+' '+size+'\n'
		f.write(path)
	except:
		print "Write Topo ERROR"
		exit(0)
	f.close()

#TODO:Identify file-type  
def file_type():
	pass

#TODO:Count the lines
def line_count():
	pass

#TODO:Identify file
def identify_file(f_path):  
	lines = null = note = size =0

	define_topo(f_path)
	_,file_type = f_path.split('.')
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


#TODO:Sort the code by lines
def code_sort():
	pass

#Walk all files
def walk_files(path):
	for root, dirs, files in os.walk(path):
		#files
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

	walk_files(rpath)
