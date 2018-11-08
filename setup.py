'''
Quick setup script.
'''
import os 

def pip_install(modules):
    for i in range(len(modules)):
        os.system('pip3 install %s'%(modules[i]))

os.system('brew install ffmpeg')
modules=['ffmpy','pandas','soundfile','pafy']
pip_install(modules)
