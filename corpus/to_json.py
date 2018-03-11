# -*- coding: utf-8 -*-
import codecs
import yaml
import json
fileopen="conversations.yaml"
data=[]
def get_data(fileopen):
	with codecs.open(fileopen, 'r',encoding='utf8') as f:
		for i in yaml.load(f)['conversations']:
			data.append(i)
get_data("conversations.yaml")
get_data("greeting.yaml")
get_data("command.yaml")
dictdata={"conversations":data}
print(dictdata)
with codecs.open('data.json', 'w',encoding='utf8') as fp:
    json.dump(dictdata, fp, ensure_ascii=False)