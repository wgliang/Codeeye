import oper,os

#TODO:Identify file
def identify_file(f_path):  
	lines = null = note = size =0
	# _,file_type = f_path.split('.')

	file_type = oper.ftype(f_path)
	date = os.stat(f_path).st_mtime
	size = os.path.getsize(f_path)

	#sort file by type
	for line in file(f_path):
		line = line.split()
		if not line:
			null = null + 1
		else:
			lines = lines + 1
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
		