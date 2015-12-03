import templates
import jsonconf
import oper

labels = ['C++', 'C', 'PHP', 'Python', 'Go', 'JavaScript', 'Shell', 'Java', 'HTML', 'Others']
def build_data_model_lines(path):
	temp  = jsonconf.read_json(path+'/conf/codeeye.json')
	data = []
	for ftype in labels:
		data.append(temp['code'][0][ftype][0]['lines'])

	ltype = [index for index in range(0,9)]

	data = data[:-1]
	templates.bar(ltype, data, 'bar-lines')
	templates.sector(data,'sector-lines')

def build_data_model_file_count(path):
	temp  = jsonconf.read_json(path+'/conf/codeeye.json')
	data = []
	for ftype in labels:
		data.append(temp['code'][0][ftype][0]['file'])

	ltype = [index for index in range(0,9)]

	data = data[:-1]
	templates.bar(ltype, data, 'bar-files')
	templates.sector(data,'sector-files')

def build_data_model_date_day(path):
	path = path+'/conf/topo.txt'
	data = oper.date_day_identify(path)
	date = [index for index in range(0,24)]
	templates.broken(date,data,'zhexiantu-today')

def build_data_model_date_week(path):
	path = path+'/conf/topo.txt'
	data = oper.date_week_identify(path)
	date = [index for index in range(1,8)]
	templates.broken(date,data,'zhexiantu-week')

def build_data_model_date_month(path):
	path = path+'/conf/topo.txt'
	data = oper.date_month_identify(path)
	date = [index for index in range(1,31)]
	templates.broken(date,data,'zhexiantu-month')


def producer(path):
	build_data_model_lines(path)
	build_data_model_file_count(path)
	build_data_model_date_week(path)
	build_data_model_date_day(path)
	build_data_model_date_month(path)
	