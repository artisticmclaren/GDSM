# GDSM
GDSM, or Geometry Dash Save Manager is a tool I wrote (with help from gd docs) to decrypt the CCLocalLevels.dat file in your save file.
# Installation

Install python from [pythons website](https://python.org/), or if you are on Linux, install it via your package manager (apt,pacman,dnf,etc), although it is likely preinstalled.

# How to use this

## levelstats.py
Run this file and enter a level name that is in the 'levels' directory to get statistics on it and specific objects. *object count is slightly innaccurate, dont know why.
## creategmd.py
This file creates a .gmd that is loadable in base GD out of decrypted level data that is stored in the 'levels' directory.
## colorstat.py
This file gets statistics on all the colors and info about the colors in a level in the 'levels' directory.
## path.txt
put the path to your Geometry Dash AppData folder (where the songs are). If you arent part of the extremely small number of people who use linux, you should change this file.

PS: at any point during the running of any of these files, you can press Ctrl+C to quit