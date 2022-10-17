# Blueprints for Text Analytics Using Python

## Machine Learning Based Solutions for Common Real World (NLP) Applications

[Jens Albrecht](https://www.linkedin.com/in/jens-albrecht), [Sidharth Ramachandran](https://www.linkedin.com/in/sidharthramachandran/), [Christian Winkler](https://www.linkedin.com/in/drchristianwinkler/)

Published by [O'Reilly, 2020](https://www.oreilly.com/library/view/blueprints-for-text/9781492074076/)

![cover](https://learning.oreilly.com/library/cover/9781492074076/250w/)

Find the book at  
[O'Reilly](https://learning.oreilly.com/library/view/blueprints-for-text/9781492074076/)  
[Amazon.com](https://www.amazon.com/Blueprints-Text-Analytics-Using-Python/dp/149207408X)  
[Amazon.de](https://www.amazon.de/Blueprints-Text-Analytics-using-Python/dp/149207408X)  
[Amazon.co.uk](https://www.amazon.co.uk/Blueprints-Text-Analytics-Using-Python/dp/149207408X)  
[Amazon.fr](https://www.amazon.fr/Blueprints-Text-Analytics-Using-Python/dp/149207408X)  
[Amazon.in](https://www.amazon.in/Blueprints-Text-Analytics-Using-Python-ebook/dp/B08PQ6MWGL/)

**If you like the book or the code examples here, please leave a friendly comment on Amazon!**  
<img src="rating.png" width="100"/>

## Download your free chapter now! 

[Free download of Chapter 7 "How to Explain a Classifier"](https://get.oreilly.com/ind_blueprints-for-text-analysis-using-python.html).


-----------------------------------------------------------------------------------

# Content of this Repository

**This repository is currently in preparation. Please do not yet send any comments.**

This repository contains the code examples of our O'Reilly book. You will find a subdirectory for each chapter containing a Jupyter notebook and additional files for the setup. 

Below you find the links to view the notebooks here on Github or execute them directly on [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb#). In the section thereafter you will find instructions to setup the environment on your local computer.

## Problems and errors

If you discover any problems or have recommendations on how to improve the code, do not hesitate to [create an issue here in the repository](https://github.com/blueprints-for-text-analytics-python/blueprints-text/issues).

For errors in the book text, please use [O'Reilly's errata page](https://www.oreilly.com/catalog/errata.csp?isbn=0636920309222).

**spaCy 3.0 and Gensim 4.0**

The book uses spaCy 2.3.2 and gensim 3.8.3. spaCy 3.0 is now officially release with several new features and a few API changes (https://spacy.io/usage/v3). Gensim 4.0 is in beta (https://github.com/RaRe-Technologies/gensim/releases). 

We are already updating our notebooks. But currently textacy is not yet supporting spaCy 3.0, although work is already in progress (see this [pull request](https://github.com/chartbeat-labs/textacy/pull/322) from us). Until textacy for spaCy 3.0 is released, you can use our own fork for the installation (see blueprints.yaml in this directory). 

## View or Run the Notebooks

For each chapter of the book we provide three links: 

  * "git" opens the notebook for viewing here on Github (sometimes not working because of [Github issue](https://github.com/jupyter/notebook/issues/3555))
  * "nbviewer" opens the notebook for viewing on nbviewer.ipython.org
  * "colab" opens a runnable copy on Google's Colab service

If you run the notebook locally or on Colab, you can execute each cell separately by hitting "Shift-enter". Do not skip cells and don't forget to run the first code cells for the setup.

  * **Chapter 1: Gaining First Insights from Textual Data**
  [[git](ch01/First_Insights.ipynb)]
  [[nbviewer](https://nbviewer.ipython.org/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch01/First_Insights.ipynb)]
  [[colab](https://colab.research.google.com/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch01/First_Insights.ipynb)]
  * **Chapter 2: Extracting Textual Insights with APIs**
  [[git](ch02/API_Data_Extraction.ipynb)]
  [[nbviewer](https://nbviewer.ipython.org/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch02/API_Data_Extraction.ipynb)]
  [[colab](https://colab.research.google.com/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch02/API_Data_Extraction.ipynb)]
  * **Chapter 3: Scraping Websites and Extracting Data**
  [[git](ch03/Scraping_Extraction.ipynb)]
  [[nbviewer](https://nbviewer.ipython.org/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch03/Scraping_Extraction.ipynb)]
  [[Colab](https://colab.research.google.com/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch03/Scraping_Extraction.ipynb)]
  * **Chapter 4: Preparing Textual Data For Statistics and Machine Learning**
  [[git](ch04/Data_Preparation.ipynb)]
  [[nbviewer](https://nbviewer.ipython.org/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch04/Data_Preparation.ipynb)]
  [[colab](https://colab.research.google.com/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch04/Data_Preparation.ipynb)]
  * **Chapter 5: Feature Engineering and Syntactic Similarity**
  [[git](ch05/Feature_Engineering_Similarity.ipynb)]
  [[nbviewer](https://nbviewer.ipython.org/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch05/Feature_Engineering_Similarity.ipynb)]
  [[Colab](https://colab.research.google.com/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch05/Feature_Engineering_Similarity.ipynb)]
  * **Chapter 6: Text Classification Algorithms**
  [[git](ch06/Text_Classification.ipynb)]
  [[nbviewer](https://nbviewer.ipython.org/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch06/Text_Classification.ipynb)]
  [[Colab](https://colab.research.google.com/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch06/Text_Classification.ipynb)]
  * **Chapter 7: How to Explain a Text Classifier**
  [[git](ch07/Explainable_AI.ipynb)]
  [[nbviewer](https://nbviewer.ipython.org/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch07/Explainable_AI.ipynb)]
  [[Colab](https://colab.research.google.com/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch07/Explainable_AI.ipynb)]
  * **Chapter 8: Unsupervised Methods: Topic Modeling and Clustering**
  [[git](ch08/Topic_Modeling_Clustering.ipynb)]
  [[nbviewer](https://nbviewer.ipython.org/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch08/Topic_Modeling_Clustering.ipynb)]
  [[Colab](https://colab.research.google.com/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch08/Topic_Modeling_Clustering.ipynb)]
  * **Chapter 9: Text Summarization**
  [[git](ch09/Text_Summarization.ipynb)]
  [[nbviewer](https://nbviewer.ipython.org/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch09/Text_Summarization.ipynb)]
  [[Colab](https://colab.research.google.com/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch09/Text_Summarization.ipynb)]
  * **Chapter 10: Exploring Semantic Relationships with Word Embeddings**
  [[git](ch10/Embeddings.ipynb)]
  [[nbviewer](https://nbviewer.ipython.org/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch10/Embeddings.ipynb)]
  [[colab](https://colab.research.google.com/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch10/Embeddings.ipynb)]
  * **Chapter 11: Performing Sentiment Analysis on Text Data**
  [[git](ch11/Sentiment_Analysis.ipynb)]
  [[nbviewer](https://nbviewer.ipython.org/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch11/Sentiment_Analysis.ipynb)]
  [[colab](https://colab.research.google.com/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch11/Sentiment_Analysis.ipynb)]
  * **Chapter 12: Building a Knowledge Graph**
  [[git](ch12/Knowledge_Graph.ipynb)]
  [[nbviewer](https://nbviewer.ipython.org/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch12/Knowledge_Graph.ipynb)]
  [[colab](https://colab.research.google.com/github/blueprints-for-text-analytics-python/blueprints-text/blob/master/ch12/Knowledge_Graph.ipynb)]
  * **Chapter 13: Using Text Analytics in Production**
  [[git](ch13/)]
  [[app](https://github.com/blueprints-for-text-analytics-python/sentiment-app)]


## Local Setup

The following instructions should work on Linux, Windows and MacOS. If you are a Windows user familiar with Linux, you should check out the [Windows Subsystem for Linux, Version 2 (WSL2)](https://docs.microsoft.com/en-us/windows/wsl/). This allows to use a Linux system on the Windows machine. However, using native Windows should also be no problem.

It is helpful to install `git` on your machine, but you can also download the full repository from Github as a zip file. If you use `git`, run the following commands from the command line:

```sh
git clone https://github.com/blueprints-for-text-analytics-python/blueprints-text.git
cd blueprints-text
```

Otherwise download the zip file, unpack it to a location convenient to you, and open a command line terminal in the project directory `blueprints-text`.

For local setup, we recommend to use [Miniconda](https://docs.conda.io/en/latest/miniconda.html), a minimal version of the popular [Anaconda](https://www.anaconda.com/) distribution that contains only the package manager `conda` and Python. Follow the installation instructions on the [Miniconda Homepage](https://docs.conda.io/en/latest/miniconda.html). If you already have Anaconda or Miniconda installed on your system: That's fine. We will create a separate virtual environment for the blueprints book so that our installation will not interfere with your previous setup.

After installation of Anaconda/Miniconda, run the following command(s) from the project directory:

```sh
conda env create --name blueprints --file blueprints.yml
conda activate blueprints
```

The prompt should change after activation and indicate that you are working in the `blueprints` environment. Our installation includes the [Jupyter notebook extensions](https://github.com/ipython-contrib/jupyter_contrib_nbextensions). We suggest to enable the extensions "table of contents" (toc2), "execute time", and "variable inspector" (varInspector):

```sh
jupyter nbextension enable toc2/main
jupyter nbextension enable execute_time/ExecuteTime
jupyter nbextension enable varInspector/main
```

Now you can start the Jupyter notebook server:

```sh
jupyter notebook
```

If working on WSL under Windows, add `--no-browser`.

Browse to the respective chapter and open the notebook file (suffix `.ipynb`)
