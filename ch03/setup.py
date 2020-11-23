#!/usr/bin/python3

import sys, os

ON_COLAB = 'google.colab' in sys.modules
if ON_COLAB:
    BASE_DIR = "/content"
    print("You are working on Google Colab.")
    print(f'Files will be downloaded to "{BASE_DIR}".')
else:
    BASE_DIR = ".."
    print("You are working on a local system.")
    print(f'Files will be searched relative to "{BASE_DIR}".')

def universal_filename(f):
    return os.path.join(BASE_DIR, f)



_DEBATES_FILE = os.path.join('data', 'un-general-debates', 'un-general-debates-blueprint.csv.gz')
DEBATES_FILE = universal_filename(_DEBATES_FILE)

if ON_COLAB:
    # there are some generic files, maybe externalize?
    required_files = [
                  'settings.py',
    ]
    print("Downloading required files ...")
    for file in required_files:
        cmd = ' '.join(['wget', '-P', os.path.dirname(BASE_DIR+'/'+file), GIT_ROOT+'/'+file])
        print('!'+cmd)
        os.system(cmd)

    print("\nAdditional setup ...")
    setup_cmds = ['pip install -r ch01/requirements.txt']

    for cmd in setup_cmds:
        print('!'+cmd)
        if os.system(cmd) != 0:
            print('  --> ERROR')
