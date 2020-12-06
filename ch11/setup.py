# setup for chapter 09 
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
        'data/amazon-product-reviews/reviews_5_balanced.json.gz',
	'ch11/requirements.txt',
	'packages/blueprints/preparation.py'
    ]

    print("Downloading required files ...")
    for file in required_files:
        cmd = ' '.join(['wget', '-P', os.path.dirname(BASE_DIR+'/'+file), GIT_ROOT+'/'+file])
        print('!'+cmd)
        if os.system(cmd) != 0:
            print('  --> ERROR')

    print("\nAdditional setup ...")
    setup_cmds = [
        'pip install torch==1.7.0+cu101 torchvision==0.8.1+cu101 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html',
	'pip install -r ch11/requirements.txt',
	'python -m nltk.downloader opinion_lexicon punkt stopwords averaged_perceptron_tagger wordnet',
	'python -m spacy download en'
    ]

    for cmd in setup_cmds:
        print('!'+cmd)
        if os.system(cmd) != 0:
            print('  --> ERROR')

elif False: # change to True to let this run
    print("\nAdditional setup (may take a few minutes) ...")
    setup_cmds = [
        'pip install torch==1.7.0+cpu torchvision==0.8.1+cpu torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html',
	'pip install -r requirements.txt',
	'python -m nltk.downloader opinion_lexicon punkt stopwords averaged_perceptron_tagger wordnet',
	'python -m spacy download en'
    ]

    for cmd in setup_cmds:
        run(cmd)
