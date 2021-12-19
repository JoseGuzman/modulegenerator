# modulegenerator 
[![CodeFactor](https://www.codefactor.io/repository/github/joseguzman/modulegenerator/badge)](https://www.codefactor.io/repository/github/joseguzman/modulegenerator)
[![GitHub license](https://img.shields.io/github/license/joseguzman/modulegenerator)](https://github.com/joseguzman/modulegenerator/blob/master/LICENSE) 
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjosejuzman%2Fmodulegenerator&count_bg=%233DC8C7&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=views&edge_flat=false)](https://hits.seeyoufarm.com)

A template to create custom Python modules for data science and research projects. For private use.

## Requirements

* Python>=3.5
* cookiecutter>=1.4.0. Cookiecutter is a Python tool which generates project folders from templates. 

```bash
pip install cookiecutter
```
To know more about cookiecutter follow this [link](https://drivendata.github.io/cookiecutter-data-science/)

## Starting a Python module
It will start a new project with a Python module when running this command at the command line. 

```bash
cookiecutter gh:joseguzman/modulegenerator
```

No need to create a directory first, cookiecutter will do it for you. The program will ask your name, email, project name and module name to create the template. 

## After installation 

Enter the folder created and type:

```bash
conda create --name module_name python=3.5 # module_name is python module
conda activate module_name #  module_name is python module
conda env export > environment.yml
pip install -e .
```

To sync it to GitHub follow the instructions  [here](https://github.com/new) and type:

```bash
git init
git add README.md
git commit -m 'first commit'
git branch -M main
git remote add origin https://github.com/user/module.git # user is GitHub user, module is python module
git push -u origin main
```

 
