import os
import sys
import urllib2
import base64
import re
from os import listdir
from os.path import isfile, join
from collections import Counter

def removeHashTag(tsvFile,path):
	listOfHashes =list()
	dictOfHashes =dict()
	hashTag = "#"
	mylist = tsvFile.split(".")
	myfile = mylist[0].split("_")
	for tag in myfile:
		hashTag = hashTag + tag
	#print "#Tag: "+ hashTag + ""
	#print "@Tag: " + "@midnight"

	fin = open(path+"\\"+tsvFile,'r+')
	for line in fin:
		line = line.replace("\t", " ")
		line = line.split(" ")
		for word in line:
			if "#" in word and hashTag not in word:
				listOfHashes.append(word)
			if "@" in word and "@midnight" not in word:
				listOfHashes.append(word)

	dictOfHashes = Counter(listOfHashes)
	#print dictOfHashes
	for d in dictOfHashes:
		print " Tag: " + d + "  " + str(dictOfHashes[d])

	fin.close()

	fin = open(path+"\\"+tsvFile,'r+')
	fout = open("aux"+hashTag+".tsv", "w+")

	for line in fin:
		for d in dictOfHashes:
			if dictOfHashes[d] > 1 :
				line = line.replace(d, "")
		line = line.replace("\t", " ")
		line = line.replace(hashTag + " ", "")
		line = line.replace(hashTag.lower(), "")
		line = line.replace("@midnight ", "")
		line = line.replace("@midnight", "")
		line = line.replace("@Midnight ", "")
		fout.write(line)

	fin.close()
	fout.close()
	
	fin = open(path+"\\"+tsvFile,'r+')
	fout = open("aux"+hashTag+".tsv", "r+")

	text = fout.read()
	#print text
	fin.seek(0)
	fin.write(text)
	fin.truncate()

	fin.close()
	fout.close()


	os.remove("aux"+hashTag+".tsv")

def main(argv):
	pathFolder=sys.argv[1]
	#print "Your path to train data is : "+ pathFolder
	#print
	onlyfiles = [f for f in listdir(pathFolder) if isfile(join(pathFolder, f))]
	#print "Here you have this files: "
	#print
	for file in onlyfiles:
		#print file
		removeHashTag(file,pathFolder)
		#print

	#print
	return 1 





if __name__ == "__main__":
   main(sys.argv[1:])