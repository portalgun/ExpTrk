
## to allow the terminal to read these commands

import subprocess
s = subprocess.getstatusoutput(f'ps -ef | grep python3')
print(s)

import argparse


