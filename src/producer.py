import templates
import jsonconf
import oper
labels = ['C++', 'C', 'PHP', 'Python', 'Go', 'JavaScript', 'Shell', 'Java', 'HTML', 'Others']
def build_data_model_lines(temp):
	data = []
	for ftype in labels:
		data.append(temp['code'][0][ftype][0]['lines'])

	return data

def build_data_model_date_day(path):
	data = oper.date_day_identify(path)
	date = [index for index in range(0,24)]
	templates.broken(date,data,'zhexiantu')

def build_data_model_date_week(temp):
	data = []
	for index,ftype in labels:
		data.append(temp['date'][0]['date-w'][index]['lines'])

	return data

def build_data_model_date_month(temp):
	data = []
	for index,ftype in labels:
		data.append(temp['date'][0]['date-m'][index]['lines'])

	return data

def build_data_model_size(temp):
	data = []
	for ftype in labels:
		data.append(temp['code'][0][ftype][0]['lines'])

	return data

def build_data_model_file_count(temp):
	data = []
	for ftype in labels:
		data.append(temp['code'][0][ftype][0]['file'])

	return data

def producer(path):
	# temp  = jsonconf.read_json(path+'/conf/codeeye.json')

	# data = build_data_model_lines(temp)
	# print data
	# data = data[:-1]
	# templates.sector(data)

	build_data_model_date_day(path+'/conf/topo.txt')