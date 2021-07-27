
## to allow the terminal to read these commands

<<<<<<< Updated upstream
import subprocess
s = subprocess.getstatusoutput(f'ps -ef | grep python3')
print(s)

import argparse
=======
!/usr/bin/env python3


import click # importing click library 

@click.group() 
def progress_bar(): # all the commands to call a progress bar in this group 
	pass 


@progress_bar.command() 
def overall_progress():
	# need to call controller here and connect to Meher's script 


	





>>>>>>> Stashed changes


