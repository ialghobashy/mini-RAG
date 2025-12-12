# mini-rag
This is a minimal implmentation of the RAG model for qustioning and answering 

## Requirements

- pythn 3.8 or later

### install python using miniconda

1) download and install Mininconda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.8
```
3) activate the environment"
```bash 
$ conda activate mini-rag
```
### (optional) Setup your command line interface for better readability 
```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```
### install the required packges 
```bash
$ pip install -r requirement.txt
```
### Set the environment variables
```bash 
$cp .env.example .env
```
set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.
