# setup for chapter 4
import os

if ON_COLAB:
    BASE_DIR = "/content"
    print("You are working on Google Colab.")
    print(f'Files will be downloaded to "{BASE_DIR}".')
else:
    BASE_DIR = ".."
    print("You are working on a local system.")
    print(f'Files will be searched relative to "{BASE_DIR}".')

if ON_COLAB:
    required_files = [
        'settings.py',
        'packages/blueprints/__init__.py',
        'packages/blueprints/exploration.py',
        'packages/blueprints/preparation.py',
        'data/reddit-selfposts/rspct_autos.tsv.gz',
        'data/reddit-selfposts/subreddit_info.csv.gz',
        'ch04/requirements.txt'
    ]

    print("Downloading required files ...")
    for file in required_files:
        cmd = ' '.join(['wget', '-P', os.path.dirname(BASE_DIR+'/'+file), GIT_ROOT+'/'+file])
        print('!'+cmd)
        if os.system(cmd) != 0:
            print('  --> ERROR')

    print("\nAdditional setup ...")
    setup_cmds = [
        'pip install -r ch04/requirements.txt',
        'python -m spacy download en_core_web_sm'
    ]
    
    for cmd in setup_cmds:
        print('!'+cmd)
        if os.system(cmd) != 0:
            print('  --> ERROR')
