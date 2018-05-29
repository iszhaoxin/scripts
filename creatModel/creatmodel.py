#!/bin/python3.5
import os,re
import sys
from mylib.texthelper import *

datasetmodel ="""import os, sys
import numpy as np
from mylib.texthelper import *

# The attribute and method self.dataMes contains
# self.fileName     self.lineNum    self.strips     self.wordDict   self.wordLis    self.wordIndex
# vocabSize(self)   word2id(self)   word2idL(self)  id2word(self)   id2wordL(self)
# wordProb(self, subsampling=True)  filter(self,threshold)          wordRandomIterator(self, size)

class Dataset:
    def __init__(self, dataPath):
        self.dataPath = dataPath
        self.dataMes = DataMes(dataPath)


if __name__ is not "__main__":
    pass
"""
modeltext = """import os, sys
sys.path.append("../data")
import numpy as np
from mylib.texthelper import *
import dataset
"""

modelName = sys.argv[1]
print(modelName)
if os.path.exists('./'+modelName) is False:
    os.mkdir('./'+modelName)
if os.path.exists('./'+modelName+'/model') is False:
    os.mkdir('./'+modelName+'/model')
if os.path.exists('./'+modelName+'/src') is False:
    os.mkdir('./'+modelName+'/src')
if os.path.exists('./'+modelName+'/data') is False:
    os.mkdir('./'+modelName+'/data')
if os.path.exists('./'+modelName+'/data/dataset') is False:
    os.mkdir('./'+modelName+'/data/dataset')
with open('./'+modelName+'/data/__init__.py', 'w') as f:
    pass

with open('./'+modelName+'/data/dataset.py', 'w') as f:
    f.write(datasetmodel)
with open('./'+modelName+'/model/model.py', 'w') as f:
    f.write(modeltext)
