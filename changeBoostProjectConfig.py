import sys
import os
from shutil import copyfile

BoostDir = sys.argv[1]
os.chdir(BoostDir)

with open('project-config.jam', 'r') as f:
    projConf=f.read().split('\n')

newProjConf = []
for line in projConf:
    if "miniconda3" in line:
        #Infer python version:
        lineWords = line.strip().split(' ')
        pyVersion= lineWords[3]
        line, _, _ = line.partition(';')
        line += ' : '+os.path.join(lineWords[5], 'include/python{}m'.format(pyVersion))+' ;'
    newProjConf.append(line)

copyfile('project-config.jam', 'project-config_original.jam')

with open('project-config.jam', 'w') as f:
    for line in newProjConf:
        f.write(line+'\n')
