# coding=utf-8
import Queue
import subprocess
import os
from subprocess import call
import sys
import time
import json

bookshelf = []

file = open("lazerson_list.txt","r")
something = ""
for line in file:
	something += line
	

something = json.loads(something)
counter = 0

for book in something:

	title = book["title"]
	image = book["images"]

	if image != None:
		subprocess.check_output(['wget','--output-document='+str(counter)+".jpg", image])


	counter += 1
	print(str(counter)+"/2181")

dir = os.path.dirname(os.path.abspath(__file__))
for filename in os.listdir(dir):
	if int(os.path.getsize(dir+"/"+filename)) == 86:
		try:
			os.remove(dir+"/"+filename)
		except OSError:
			pass

counter = 0

for book in something:
	title = book["title"]
	image = book["images"]

	fname = dir+"/"+str(counter)+".jpg"
	if not os.path.isfile(fname):
		print("image "+fname+" not found.  Generating it.")
		if len(title) > 35:
			title = title[:30] + "..."
	
		subprocess.check_output(["convert", "default_book.svg", "-gravity", "center","-font","Courier","-pointsize","13","caption:"+title, "-compose","over","-composite",str(counter)+".gif"])
	else:
		subprocess.check_output(["convert", fname, str(counter)+".gif"])
	book["images"] = '<img src="'+str(counter)+'.gif">'

	counter+=1
	print(counter)


something = json.dumps(something, sort_keys=True, indent=4, separators=(',', ': '))



file.close
file = open("new.JSON","w")
file.write(str(something) + "\n")
file.close()

