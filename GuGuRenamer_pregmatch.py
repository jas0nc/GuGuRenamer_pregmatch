#!/usr/local/bin/python3
# GuGuRenamer(pregmatch)
# coding="utf-8"

# ----------------------------------------------------------------------------------
# How to use this Script
# 0) Install Python3 in package Center
# 1) Place this GuGuRenamer folder inside the Anime Directory
# 2) if you want to only rename file in one specific folder, please copy the absolute path to below:
# 2) Otherwise, this script will scan all folders next to GuGuRenamer folder
# eg. specificpath = "/volume1/Multimedia/Animation/Sword Art Online"
path = ""
# 3)spcific filetype for files needed to be renamed
types = ('*.mkv', '*.mp4')
# 4) Check the full path to the GuGuRenamer_pregmatch.py eg. "/volume1/Multimedia/Animation/GuGuRenamer/GuGuRenamer_pregmatch.py"
# 5) Run this script, enter the below cmd in ssh or in Synology DSM->scheduled task->new user-defined script->as root,
#	ie. .<full path to GuGURenamer.py>
#	eg. ./volume1/Anime/Anime/GuGuRenamer/GuGuRenamer_pregmatch.py
# ----------------------------------------------------------------------------------

import glob, re, os, sys

#define path to scan
if not path:
	path = os.path.dirname(os.path.abspath(__file__))+"/../**/"
else:
	path = path
print("Scanning: " + path) #for debug use

#serach files with specified filetype
files_grabbed = []
for files in types:
	files_grabbed.extend(glob.glob( path + files))
	files_grabbed.extend(glob.glob( path + "**/" + files))
	files_grabbed.extend(glob.glob( path + "/**/**/" + files))
files_grabbed   # the list of pdf and cpp files
#print(files_grabbed) #for debug use
#sys.exit("Stop for Debug")

#start rename process
for filename in files_grabbed:
   #duplicate filename to new_name
	new_name = filename
	process = ""
	if re.search('\s-\s\d+', new_name):
		process += ' " - XX"  => " EXX ";'
		def replacenum(matched):
			value = int(matched.group('value'))
			return " E" + str('{:02d}'.format(value)) + " "
		new_name = re.sub('\s-\s(?P<value>\d+)',replacenum,new_name)
	if re.search('\[\d+\]', new_name):
		process += ' "[XX]"  => " EXX ";'
		def replacenum(matched):
			value = int(matched.group('value'))
			return " E" + str('{:02d}'.format(value)) + " "
		new_name = re.sub('\[(?P<value>\d+)\]',replacenum,new_name)
	if re.search('\sS\d+\s', new_name):
		process += ' " SXX "  => " SXX";'
		def replacenum(matched):
			value = int(matched.group('value'))
			return " S" + str('{:02d}'.format(value)) + ""
		new_name = re.sub('\sS(?P<value>\d+)\s',replacenum,new_name)
	if re.search('\s\d+\]\s', new_name):
		process += ' " XX] "  => " SXX";'
		def replacenum(matched):
			value = int(matched.group('value'))
			return " S" + str('{:02d}'.format(value)) + ""
		new_name = re.sub('\s(?P<value>\d+)\]\s',replacenum,new_name)
	if re.search('\_\d+\]\s', new_name):
		process += ' "_XX] "  => " SXX";'
		def replacenum(matched):
			value = int(matched.group('value'))
			return " S" + str('{:02d}'.format(value)) + ""
		new_name = re.sub('\_(?P<value>\d+)\]\s',replacenum,new_name)
	if re.search('\sII\]\s', new_name):
		process += ' " II] "  => " S02";'
		def replacenum(matched):
			#value = int(matched.group('value'))
			return " S" + str('{:02d}'.format(2)) + ""
		new_name = re.sub('\sII\]\s',replacenum,new_name)
	if re.search('\sIII\]\s', new_name):
		process += ' " III] "  => " S03";'
		def replacenum(matched):
			#value = int(matched.group('value'))
			return " S" + str('{:02d}'.format(3)) + ""
		new_name = re.sub('\sIII\]\s',replacenum,new_name)
	if (filename != new_name):
		#rename the file
		os.rename(filename, new_name)
		print ("	OLD-Name: "+ filename)
		print ("	Handling:  " + process)
		print ("	NEW-Name: " + new_name)

sys.exit("End: GuGuRenamer Execution Completed")
