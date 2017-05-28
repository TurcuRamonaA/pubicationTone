import os
import sys
import urllib2
import base64
import re
from os import listdir
from os.path import isfile, join
from collections import Counter
import string
from string import digits
def create_corpus(tsvFile,path):
	fin = open(path+"\\"+tsvFile,'r+')
	fout = open("corpus_multi_word.txt", "w+")
	for line in fin:
		cost = "0"
		#print line
		line = line.replace("\t", " ")
		line = line.split(" ")
		mylist = list()
		cost = line[-1]
		print "LINE :: :: :: "+line[-1]
		for word in line:
			
			if not word.isdigit():
				if word and not word.isspace() and not "\n" in word:
					#print word
					mylist.append(word)
			if word.isdigit():
				print "###########" + word
				if int(word)<3:
					cost = word
					print "###########"+word
		print mylist
		print "COST = " + cost
		for x in mylist:
			for y in mylist:
				if not x in y:
					line = "\"" + x + " " + y + "\"" + ":" + str(cost) + ","
					print line
					fout.write(line)
	fout.close()

def pprocTweet(tweet):
	tweet = tweet.lower()
	tweet = tweet.translate(None, string.punctuation)
	tweet = tweet.translate(None, digits)
	words = tweet.split(" ")
	#for word in words:
		#print word
	return words

def main(argv):
	pathFolder=sys.argv[1]
	print "Your path to train data is : "+ pathFolder
	print
	onlyfiles = [f for f in listdir(pathFolder) if isfile(join(pathFolder, f))]
	print "Here you have this files: "
	print
	for file in onlyfiles:
		print "FILE: " + file
		create_corpus(file,pathFolder)
		print

	print
	return 1 





if __name__ == "__main__":
   main(sys.argv[1:])