## to allow the terminal to read these commands

import click # importing click library 

#from controller import controller

# all the control send is options 

@click.command() 
@click.option('-sum','--summary', show_default=True, help='Summary of the progress') ## defaults 
@click.option('-Db', show_default=True)
@click.option('--connect', show_default=True)
@click.option('--host', show_default=True)
@click.option('-wd', show_default=True, help='Enter the variable for which you want the working directory') ## system options
@click.option('--project', show_default=True, help='Project name') ## initializers 
@click.option('--researcherName', show_default=True, help='Researcher name')
@click.option('--experiment', show_default=True, help='Experiment name e.g. Oddball, Cyberball, IAPS, ABE, etc') ## experiment options 
@click.option('-ev', '--experimentversion', default = 0.0, type=float, show_default=True, help='Version of this task') # create an if - if default then output their version if not default update the version 
@click.option('-r','--run', default=0, type=int, show_default=True, help='Current run') # output what run they are in if no argument entered
@click.option('-tr','--totalruns', default=0, type=int, show_default=True, help='Total runs for this task') # if default output 0 if previously nothing entered or output total stored or if not 0 update total
@click.option('-ts', '--totalsubjects', default=0, type=int, show_default=True, help='Total subjects for the experiment') ## subject options # if default output total if not update default 
@click.option('-s', '--subid', default=0, type=int, show_default=True, help='Subject ID') # if default return id if not enter pass it to controller 
@click.option('-st', '--stimuliset', nargs=2, show_default=True, help='Enter the name of your stimuli set and what task it is associated with') ## stimuli set options # if task input is All make it associate with all tasks 
@click.option('-stv', '--stimsetversion', default=0.0, type=float, show_default=True, help='Enter the version of the stimuli set')
@click.option('-sto', '--stimtest', default=False, type=bool, show_default=True, help='If this is your own stimuli set, enter True') 
@click.option('-stnum','--stimnum', default=0.0, type=float, show_default=True, help='Enter the number for this stimuli, to retrive the number leave argument blank') # if default spit out stimuli number if not enter it and associate it with current stim through controller 
@click.option('-sn','--subjectnote', type=(int, str), show_default=True, help='Enter the subjectid for whom you want to leave a note and then enter the note within ""') ## notes options # get prompt for user input if not default value 
@click.option('-rn'.'--runnote', type=(float, str) , show_default=True, help='Enter the run number for which you want to leave a note and then enter the note within ""') #same if statement as above 
@click.option('-vn','--versionnote', type=(float, str), show_default=True, help='Enter the version number for which you want to leave a note and then enter the note in ""') ## ^^ ( can create a function for this note section)
@click.option('-stn','--stimulinote', nargs=2, type=(float,str), show_default=True, help='Enter the number of the stimuli and the note you want to leave within ""') 
@click.option('-rs','--remsub', default=0, show_default=True, help='Leave blank to get remaining subjects') ## remaining options #if default output number if not invalid - create calculatore for how many subjects pending 
@click.option('-fs','--finishedsub', default=0, show_default=True, help='Leave blank to get number of subjects run') # same as above 
@click.option('-rr','--remruns', default=0, show_default=True, help='Leave blank to get how many runs left') # same as above 
@click.option('-fr','--finishedruns', default=0, show_default=True, help='Leave blank to get number of runs run') # same as above
@click.option('-u', '--update', show_default=True, help='Variable that needs updating') ## update - set up an if loop for this with the a prompt - what is the new value. we need a variable list 
@click.option('-p', show_default=True, help='Progress bar options: overall, collection, analysis, writing') ## progress options 
@click.option('-ps', show_default=True, help='Progress summary for: overall, collection, analysis, writing') 
def tracker(): # summary inputs can be: overall, collection, subjects, analysis, publication/writing
	# contr=controller(debug)
	# contr.send_msg("myDb","connect",host=dbhost, port=dbport, password=dbpassword)
	click.echo("Progress bar being calculated"





## stimuli set 
## experiment information
## subject 
## remaining





# commands for outputs 

# @click.command()
# @click.argument(stimuli_information)
# if __name__ == '__main__':
#     random()
# commands for summaries 
# op