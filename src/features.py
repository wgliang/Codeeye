import oper,os

#Identify file
def identify_file(f_path):  
	lines = null = note = size =0

	file_type = oper.ftype(f_path)

	date = os.stat(f_path).st_ctime

	size = os.path.getsize(f_path)

	root = os.getcwd()
	rtemp = root.rfind('/src')
	temp = root[:rtemp].rfind('/')
	fpath = root[:rtemp] + '/' + 'conf/' +root[temp+1:rtemp].lower() + '.json'

	#sort file by type
	for line in file(f_path):
		line = line.split()
		if not line:
			null = null + 1
		else:
			lines = lines + 1

	oper.json_rewrite(fpath, file_type, lines, note, null, date)

	oper.define_result(f_path, file_type, lines, note, null, date, size)

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
		