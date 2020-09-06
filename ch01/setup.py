# setup for chapter 01
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
    # there are some generic files, maybe externalize?
    required_files = [
        'settings.py',
        'data/un-general-debates/un-general-debates-blueprint.csv.gz',
        'ch01/requirements.txt'
    ]
                  
    print("Downloading required files ...")
    for file in required_files:
        cmd = ' '.join(['wget', '-P', os.path.dirname(BASE_DIR+'/'+file), GIT_ROOT+'/'+file])
        print('!'+cmd)
        if os.system(cmd) != 0:
            print('  --> ERROR')

    print("\nAdditional setup ...")
    setup_cmds = [f'mkdir -p {BASE_DIR}/data/un-general-debates',
                  'pip install -r ch13/colab_requirements.txt',
                  'python -m spacy download en']

    for cmd in setup_cmds:
        print('!'+cmd)
        if os.system(cmd) != 0:
            print('  --> ERROR')
           