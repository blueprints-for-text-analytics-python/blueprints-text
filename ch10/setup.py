# setup for chapter 10
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
        'packages/blueprints/embeddings.py',
        'data/reddit-selfposts/reddit-selfposts-ch10.db',
        'ch10/requirements.txt'
    ]

    print("Downloading required files ...")
    for file in required_files:
        cmd = ' '.join(['wget', '-P', os.path.dirname(BASE_DIR+'/'+file), GIT_ROOT+'/'+file])
        print('!'+cmd)
        if os.system(cmd) != 0:
            print('  --> ERROR')

    print("\nAdditional setup ...")
    setup_cmds = [f'pip install -r {BASE_DIR}/ch10/requirements.txt',
                  'mkdir -p models']

    for cmd in setup_cmds:
        print('!'+cmd)
        if os.system(cmd) != 0:
            print('  --> ERROR')
