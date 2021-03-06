#Conversion of json format to yaml format
from yaml.resolver import BaseResolver
import yaml
#importing data from runn
from runn import para as data
class AsLiteral(str):
    pass

def represent_literal(dumper, data):
    return dumper.represent_scalar(
        BaseResolver.DEFAULT_SCALAR_TAG, data, style="|"
    )

#Writing the data into nlu.yml 
def create_yml(path, data):
    with open(path, "w") as ymls:
        #converting data into yaml format
        yaml.dump(data, ymls, default_flow_style=False, sort_keys=False, width=700)


import json 

yaml.add_representer(AsLiteral, represent_literal)    
#preparing of data    
def toformat(data):
    temp=[]
    for each in data:  
        result = {"intent":each.get("intent")}
        utterstr = AsLiteral(yaml.dump(each.get("examples"), width=1000))
        result["examples"] = utterstr
        temp.extend([result])
    return temp

data  = toformat(data)
print(data)
nlu = {"version":"3.0", "nlu":data}
path = r'data/nlu.yml'
create_yml(path,nlu)
