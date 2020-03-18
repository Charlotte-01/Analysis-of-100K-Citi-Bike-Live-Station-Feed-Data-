from datetime import datetime, date
from elasticsearch import Elasticsearch

def create_index(index_name):
	es = Elasticsearch()
	try:
		es.indices.create(index = index_name)
	except:
		pass
	return es

def push_record(record, es, index_name):
	for key, value in record.items():
		if '_amount' in key:
			record[key] = float(value)
		elif '_date' in key:
			try:
				record[key] = datetime.strptime(value,'%m/%d/%Y').date()
			except:
				try:
					m, d, y = map(int, record[key].split('/'))
					if m == 2 and d == 29 and y % 4:
						m, d = 3, 1
						record[key] = datetime.date(y, m, d)
				except:
					pass
	es.index(index=index_name, id=record['summons_number'], body=record)
