#!/usr/bin/env python3

# This file controls the Progress Bar for ExpTrk
# It interfaces with all the different parts of the 'Controller' to obtain 'Progress Updates' for the different submodules
#

import numpy as np

class allProgBar:
    
    # Initialises parameters to create the progress bar
    def __init__(self, max = 20, message='Progress for ::', start ='[', stop = ']', fill = '=', blank = '_', arrow = '>') -> None:
        self.max = max
        self.message = message
        self.arrow = arrow
        self.start = start
        self.fill = fill
        self.blank = blank
        self.stop = stop

# Obtain Progress Updates for each submodule
#
#   1. Automated Data collected
#   2. Subject and Experiment Descriptors
#   3. Data Collection Variables
#   4. Results Fields
#   5. Analysis-related Fields
#   6. Post-completion-related Fields (i.e. publication, data archiving, open-access)
#
    def calc_completed(self, filled, total):
        completed = np.ceil((filled / total) * 20).astype(int)
        return completed

    def auto_prog(self):
        # Check progress on automated data collected
        label = " Automated Progress :: "
        return label

    def desc_prog(self):
        # Check progress on user insertion of experiment descriptors
        label = " Descriptor Progress :: "
        return label

    def datacollection_prog(self):
        # Check progress on data collection
        label = " Data Collection Progress :: "
        return label

    def results_prog(self):
        # Check progress on results generated
        label = " Results Progress :: "
        return label

    def print_prog(self, f1, t1, f2, t2, f3, t3, f4, t4):
        # Print progress bars for all modules
        print(self.message + self.auto_prog() + self.start + (self.calc_completed(f1, t1) * self.fill) + self.arrow + ((self.max - self.calc_completed(f1, t1)) * self.blank) + self.stop)
        print(self.message + self.desc_prog() + self.start + (self.calc_completed(f2, t2) * self.fill) + self.arrow + ((self.max - self.calc_completed(f2, t2)) * self.blank) + self.stop)
        print(self.message + self.datacollection_prog() + self.start + (self.calc_completed(f3, t3) * self.fill) + self.arrow + ((self.max - self.calc_completed(f3, t3)) * self.blank) + self.stop)
        print(self.message + self.results_prog() + self.start + (self.calc_completed(f4, t4) * self.fill) + self.arrow + ((self.max - self.calc_completed(f4, t4)) * self.blank) + self.stop)