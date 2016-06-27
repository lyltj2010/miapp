# coding:utf-8
import json
class JsonOutputer(object):
	def __init__(self):
		# init a list to contain list of dicts 
		self.data = []

	def collect_data(self, data):
		if data is None:
			return
		self.data.append(data)

	def output_json(self,name):
		with open(name,'w') as fout:
			json.dump(self.data, fout)

