# setup for chapter 02 
import os, sys
from subprocess import Popen, PIPE

if ON_COLAB:
    BASE_DIR = "/content"
    print("You are working on Google Colab.")
    print(f'Files will be downloaded to "{BASE_DIR}".')
else:
    BASE_DIR = ".."
    print("You are working on a local system.")
    print(f'Files will be searched relative to "{BASE_DIR}".')

def run(cmd):
    print('!'+cmd)
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        print('  --> ERROR')
        print(stdout.decode())
        print(stderr.decode())

if ON_COLAB:
    required_files = [
        'settings.py',
	'packages/blueprints/exploration.py',
	'ch02/requirements.txt'
    ]

    print("Downloading required files ...")
    for file in required_files:
        cmd = ' '.join(['wget', '-P', os.path.dirname(BASE_DIR+'/'+file), GIT_ROOT+'/'+file])
        print('!'+cmd)
        if os.system(cmd) != 0:
            print('  --> ERROR')

    print("\nAdditional setup ...")
    setup_cmds = [
        'pip install -r ch02/requirements.txt',
	'python -m nltk.downloader stopwords'
    ]

    for cmd in setup_cmds:
        print('!'+cmd)
        if os.system(cmd) != 0:
            print('  --> ERROR')

elif False:# change to True to let this run
    print("\nAdditional setup (may take a few minutes) ...")
    setup_cmds = [
        'pip install -r requirements.txt',
	'python -m nltk.downloader stopwords'
    ]

    for cmd in setup_cmds:
        run(cmd)
