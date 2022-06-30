import os
from pprint import pprint
path = r'\read and write homework\test' 
def reader():
    for filename in os.listdir(path):
        with open(os.path.join(path, filename), encoding='utf-8')as f:
            text = f.readlines()
            data = dict({'name':filename, 'line':len(text), 'text':text})
    return data   



print(reader())    
    
    
         
