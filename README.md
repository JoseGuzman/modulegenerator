# modulegenerator 

A template to create custom Python modules for data science and research projects. For private use.

## Requirements

* Python>=3.5
* cookiecutter>=1.4.0. Cookiecutter is a Python tool which generates project folders from templates. 

```bash
$ pip install cookiecutter
```
To know more about cookiecutter follow this [link](https://drivendata.github.io/cookiecutter-data-science/)

## Starting a Python module
It will start a new project with a Python module when running this command at the command line. 

```bash
$ cookiecutter gh:JoseGuzman/modulegenerator
```

No need to create a directory first, cookiecutter will do it for you. The program will ask your name, email, project name and module name to create the template. 

## After installation 

Enter the folder created and type:

```bash
$ conda create --name module_name python=3.5 # module_name is python module
$ conda activate module_name #  module_name is python module
$ conda env export > environment.yml
$ pip install -e .
```

To sync it to GitHub follow the instructions  [here](https://github.com/new) and type:

```bash
$ git init
$ git add README.md
$ git commit -m 'first commit'
$ git branch -M main
$ git remote add origin https://github.com/user/module.git # user is GitHub user, module is python module
$ git push -u origin main
```

 
