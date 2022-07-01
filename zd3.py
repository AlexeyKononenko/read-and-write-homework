import os
from pprint import pprint
path = r'\read and write homework\test' 
def reader():
    all_data = {}
    data = {}
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), encoding='utf-8')as f:
            text = f.readlines()
            data[filename] = (len(text), text)
            all_data.update(data)
    return all_data

pprint(reader())    
    
def sorted_dict():
    sorted_file = sorted(reader().items(), key=lambda x:x[1])
    print(sorted_file)
    return sorted_file   
         
pprint(sorted_dict())