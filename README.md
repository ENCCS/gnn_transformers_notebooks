# Notebook material for the ENCCS Graph Neural Networks and Transformers workshop

This repository contains the notebooks for the ENCCS course on Graph Neural Networks and Transformers. There are two version of the notebooks, one intended to be run on Google Colab (under the colab directory) and one intended to be run locally (under the session_1 to session_4 directories).

## Installing the dependencies

You need an Anaconda (or conda forge) installation before proceding.

If you run the local files, you need to install the dependencies. These are in conda environment files. Depdending on what GPU you have, run the below commands in a shell:

 ### NVIDIA GPU:
```shell
conda env create - f cuda_environment.yml
```
 ### AMD GPU:
```shell
conda env create -f rocm_environment.yml
```

Once the environment has been created, activate it by running

```shell
conda activate gnnt
```
    
And start the jupyter notebook server:

```shell
jupyter notebook
```

