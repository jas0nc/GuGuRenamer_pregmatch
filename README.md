# GuGuRenamer_pregmatch
This GuGuRenamer use prematch to replace the need of Dictionary

This is a second version of gugurenamer (https://github.com/jas0nc/GuGuRenamer).

But it use pregmatch to rename instead of dictionary.

# ----------------------------------------------------------------------------------
$ Supported rename format
Currently support the below filename format renaming:
" - XX"  => " EXX "

"[XX]"  => " EXX "

" SXX "  => " SXX"

" XX] "  => " SXX"

"_XX] "  => " SXX"

" II] "  => " S02"

" III] "  => " S03"

(Please suggest if you find any new format needed to be rename)

# ----------------------------------------------------------------------------------
# How to use
The way to use this GuGuRenamer_pregmatch.py is basically the same as gugurenamer.py.
How to use this Script
0) Install Python3 in package Center
1) Place this GuGuRenamer folder inside the Anime Directory
2) if you want to only rename file in one specific folder, please copy the absolute path to below:
2) Otherwise, this script will scan all folders next to GuGuRenamer folder
eg. path = "/volume1/Multimedia/Animation/Sword Art Online"
3)spcific filetype for files needed to be renamed
eg. types = ('*.mkv', '*.mp4')
4) Check the full path to the GuGuRenamer_pregmatch.py eg. "/volume1/Multimedia/Animation/GuGuRenamer/GuGuRenamer_pregmatch.py"
5) Run this script, enter the below cmd in ssh,
ie. .<full path to GuGuRenamer_pregmatch.py>
eg. ./volume1/Anime/Anime/GuGuRenamer/GuGuRenamer_pregmatch.py
5.2)  or in Synology DSM->scheduled task->new user-defined script->as root,
export LANG=en_US.UTF-8
/usr/local/bin/python3 <GuGuRenamer_pregmatch.py Location>
