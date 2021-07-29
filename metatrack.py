## to allow the terminal to read these commands

import click # importing click library 

#from controller import controller

# all the control send is options 

@click.command() 
@click.option('-s', show_default=True, help='Summary of the progress') ## defaults 
@click.option('-Db', show_default=True)
@click.option('--connect', show_default=True)
@click.option('--host', show_default=True)
@click.option('--project', show_default=True, help='Project name') ## initializers 
@click.option('-rn', '--researcherName', show_default=True, help='Researcher name')
@click.option('--experiment', show_default=True, help='Experiment name e.g. Oddball, Cyberball, IAPS, ABE, etc') ## experiment options 
@click.option('-ev', '--experimentversion', default = 0.0, type=float, show_default=True, help='Version of this task') # create an if - if default then output their version if not default update the version 
@click.option('-r','--run', default=0, type=int, show_default=True, help='Current run') # output what run they are in if no argument entered
@click.option('-tr','--totalruns', default=0, type=int, show_default=True, help='Total runs for this task') # if default output 0 if previously nothing entered or output total stored or if not 0 update total
@click.option()





@click.option('-u', '--update', show_default=True, help='Variable that needs updating') ## update - set up an if loop for this with the a prompt - what is the new value. we need a variable list 
@click.option('-p', show_default=True, help='Progress bar options: overall, collection, analysis, writing') ## user output help from here on out 
@click.option('-ps', show_default=True, help='Progress summary for: overall, collection, analysis, writing')


def tracker(): # summary inputs can be: overall, collection, subjects, analysis, publication/writing
	# contr=controller(debug)
	# contr.send_msg("myDb","connect",host=dbhost, port=dbport, password=dbpassword)
	click.echo("Progress bar being calculated"





## stimuli set 
## experiment information
## subject 
## 





# commands for outputs 

# @click.command()
# @click.argument(stimuli_information)
# if __name__ == '__main__':
#     random()
# commands for summaries 
# op