#!/usr/bin/env python3

## to allow the terminal to read these commands

## filter out separate arguments to make sure goes cleanly into the controller 


import click # importing click library 

## command groups 


# to see if this works 


# @click.command()
# @click.option('-v', '--value', 
#               prompt=True, multiple=True)
# def cli(value):
#     print(value)  # just print the value

# if __name__ == '__main__':
#     # supporing env vars
#     cli.main(auto_envvar_prefix='TEST')


# @click.command()
# def random():
#     @click.echo("Hello")


# command for initialization 

@click.command() ## command called when starting a new project with exptrk
@click.option() ## make the db options 
@click.argument() 
def initialize():
	project_name = click.prompt('Please enter your project name. If it is an existing project, please enter the exact name of it.', type=str)
	researcher_name = click.prompt('Please enter your name', type=str)
	stimuli_use = click.prompt('Are you using your own stimuli set', type=bool)
	Controller.parse(dbuser, dbpassword, dbhost, dbport)
	Controller.parse(project_name, researcher_name, stimuli_use)


command for project update

@click.command()
@click.argument('variable_name', type=str) # variable that needs to be updated 
@click.argument('update', type=str) # what information needs to be updated
def update(variable_name, update):





command for progress bar 

@click.command() 
@click.option('--summary', default=1, help='Summary of the progress') 
@click.argument('progress_type')
def progress(summary, progress_type): # summary inputs can be: overall, collection, subjects, analysis, publication/writing
	Controller.parse('progress', summary, progress_type)


commands for outputs 

@click.command()
@click.argument(stimuli_information)
# if __name__ == '__main__': don't need this since have the setup file available 
#   progress()
# commands for summaries 
# options list 
-v - version