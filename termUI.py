#!/usr/bin/env python3
## to allow the terminal to read these commands
# (gotta have a hash in front of it and tippy top) -Dave

## filter out separate arguments to make sure goes cleanly into the controller 



import click # importing click library 

## command groups 

@click.group() 
def progress_bar(): # all the commands to call a progress bar in this group 
	pass 


## commands for progress bar 

@click.command() 
@click.option('--summary', default=0, help='Summary of the progress') 
@click.argument('progress_type')
def progress(summary, progress_type): # summary inputs can be: overall, collection, subjects, analysis, publication/writing
	Controller.parse('progress', summary, progress_type)


if __name__ == '__main__':
    progress()

    



## commands for summaries 



	








