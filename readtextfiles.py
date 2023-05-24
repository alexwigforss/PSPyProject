from readimages import getTxtFileNames as gtf
import os
path = os.getcwd() + '\\' + 'text\\'
textfiles = gtf()

for e in textfiles:
    print(path + e)