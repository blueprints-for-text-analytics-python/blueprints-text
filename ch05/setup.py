#!/usr/bin/python3

import sys, os

GIT_ROOT = 'https://github.com/blueprints-for-text-analytics-python/blueprints-text/raw/master'

# this is generic, maybe externalize?
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



_ABCNEWS_FILE = os.path.join('data', 'abcnews', 'abcnews-date-text.csv.gz')
ABCNEWS_FILE = universal_filename(_ABCNEWS_FILE)

if ON_COLAB:
    # there are some generic files, maybe externalize?
    required_files = [
                  'settings.py',
                  _ABCNEWS_FILE,
                  'ch05/requirements.txt'
    ]
    print("Downloading required files ...")
    for file in required_files:
        cmd = ' '.join(['wget', '-P', os.path.dirname(BASE_DIR+'/'+file), GIT_ROOT+'/'+file])
        print('!'+cmd)
        os.system(cmd)

    print("\nAdditional setup ...")
    setup_cmds = ['pip install -r ch05/requirements.txt',
                  'python -m spacy download en']

    for cmd in setup_cmds:
        print('!'+cmd)
        if os.system(cmd) != 0:
            print('  --> ERROR')

