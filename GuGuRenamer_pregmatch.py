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
types = ('*.mkv', '*.mp4', '*.ass', '*.srt')
# 4) Check the full path to the GuGuRenamer_pregmatch.py eg. "/volume1/Multimedia/Animation/GuGuRenamer/GuGuRenamer_pregmatch.py"
# 5) Run this script, enter the below cmd in ssh or in Synology DSM->scheduled task->new user-defined script->as root,
#	ie. .<full path to GuGURenamer.py>
#	eg. ./volume1/Anime/Anime/GuGuRenamer/GuGuRenamer_pregmatch.py
# ----------------------------------------------------------------------------------

import glob, re, os, sys, csv

#define path to scan
if not path:
	path = os.path.dirname(os.path.abspath(__file__))+"/../**"
else:
	path = path
print("Scanning: " + path) #for debug use

#serach files with specified filetype
files_grabbed = []
for files in types:
	files_grabbed.extend(glob.glob( path + "/" + files))
	files_grabbed.extend(glob.glob( path + "/**/" + files))
	files_grabbed.extend(glob.glob( path + "/**/**/" + files))
files_grabbed   # the list of pdf and cpp files
#print(files_grabbed) #for debug use
#sys.exit("Stop for Debug")

################################################

# define dictionay as dictionary
dictionary = {}

#open the Dictionary.csv file with using utf-8 coding
reader = csv.reader(open( os.path.dirname(os.path.abspath(__file__))+'/Dictionary_prematch.csv', 'r', encoding="utf-8"))
#print("Dict: " + os.path.dirname(os.path.abspath(__file__))+'/Dictionary.csv') #for debug use

#put result of csv.reader to the Dictionary
for dmhyname, plexname in reader:
   dictionary[dmhyname] = plexname

################################################

#start rename process
for filename in files_grabbed:
   #duplicate filename to new_name
	old_name = os.path.basename(filename)
	new_name = os.path.basename(filename)
	location = os.path.split(os.path.abspath(filename))[0] + "/"
	process = ""
	if re.search('Alicization War of Underworld\s-\s\d+', new_name):
		process += ' "Alicization War of Underworld - XX"  =>Alicization War of Underworld " S04EXX(-24) ";'
		def replacenum(matched):
			value = int(matched.group('value'))-24
			return " S04E" + str('{:02d}'.format(value)) + " "
		new_name = re.sub('\s-\s(?P<value>\d+)',replacenum,new_name)
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

	for key in dictionary:
		#print("Dict(Find)") #for debug use
		#print(key) #for debug use
		#print("Dict(Repl)") #for debug use
		#print(dictionary[key]) #for debug use

		#prepare the new_name for renaming
		if new_name.find(key):
			new_name = new_name.replace(key, dictionary[key])
			#process += 'Found "' + key + '" => Replace to "' + dictionary[key] + '";'

	#print result if renamer has renamed any file
	if (old_name != new_name):
		#rename the file
		os.rename(location + old_name, location+new_name)
		print ("	OLD-Name: "+ location + old_name)
		print ("	Handling:  " + process)
		print ("	NEW-Name: " + location + new_name)

sys.exit("End: GuGuRenamer Execution Completed")
