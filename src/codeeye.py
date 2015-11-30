import sys,os,time,commands  
import sorts
import oper
import features
import producer
from optparse import OptionParser

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
		# rpath = os.getcwd()
		print 'Not take dirs'
		exit(0)
	oper.free_result(rpath)
	oper.json_init(rpath+'/conf/codeeye.json')
	features.walk_files(rpath)
	res = oper.read_result(rpath+'/conf/topo.txt')
	producer.producer(rpath)

