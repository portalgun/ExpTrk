
## to allow the terminal to read these commands

## filter out separate arguments to make sure goes cleanly into the controller 

!/usr/bin/env python3


import click # importing click library 

## command groups 

@click.group() 
def progress_bar(): # all the commands to call a progress bar in this group 
	pass 


# to see if this works 

@click.command()
def random():
    @click.echo("Hello")


# command for progress bar 

@click.command() 
@click.option('--summary', default=0, help='Summary of the progress') 
@click.argument('progress_type')
def progress(summary, progress_type): # summary inputs can be: overall, collection, subjects, analysis, publication/writing
	Controller.parse('progress', summary, progress_type)



## if __name__ == '__main__': don't need this since have the setup file available 
 ##   progress()





## commands for summaries 



	








