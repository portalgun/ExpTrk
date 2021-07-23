

1 Minimum Reqs
--------------

Database follows project hierarchy
Experiment Data saving follows project hierarchy
Should non-hierarchical data be stored in a separate database?

Hierarchical structures
SuperProject -> project -> subproject      -> ... -> experiment -> subject -> experiment mode -> {data, ...}

- maybe split at experiment?

Non-hierarchical - gain in performance?

1. subject

2. experiment details

1.1 Fields
~~~~~~~~~~

name
author
creation date
total trials
subjects
related papers
description
randomization parameters
repository
    dev branch
    experiment branch
running options
    language
        functions
            parameters
            parameters file
        path
        stimuli
data saving method
blocks
exp type
    psychophysical
        2IFC
            n standards
            n comparisons/standard
    matching
expmodes

1.2 general options
~~~~~~~~~~~~~~~~~~~

default base saving directories

1.3 Display mode
~~~~~~~~~~~~~~~~

tree mode
single level mode (subject mode & experiment mode)

Sortable by any field
   project hierarchy
   parameters
