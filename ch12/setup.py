# setup for chapter 12
import os, sys
from subprocess import Popen, PIPE

ON_COLAB = 'google.colab' in sys.modules

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
        'ch12/requirements.txt',
        'packages/blueprints/__init__.py',
        'packages/blueprints/preparation.py',
        'packages/blueprints/knowledge.py',
    ]

    print("Downloading required files ...")
    for file in required_files:
        cmd = ' '.join(['wget', '-P', os.path.dirname(BASE_DIR+'/'+file), GIT_ROOT+'/'+file])
        run(cmd)

    print("\nAdditional setup (may take a few minutes) ...")
    setup_cmds = [
        f'pip install -r ch12/requirements.txt',
        'mkdir -p figures',
        'python -m spacy download en_core_web_sm',
        'python -m spacy download en_core_web_lg'
    ]

    for cmd in setup_cmds:
        run(cmd)
        
elif False: # change to True to let this run
    print("\nAdditional setup (may take a few minutes) ...")
    setup_cmds = [
        'pip install -r requirements.txt',
        'python -m spacy download en_core_web_sm',
        'python -m spacy download en_core_web_lg'
    ]

    for cmd in setup_cmds:
        run(cmd)
