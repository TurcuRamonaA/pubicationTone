#! /usr/bin/env python2.7
import os
import sys
import urllib2
import base64
import re
import dict_corpus
import string
import parser_for_train_data
import celeb_corpus
import dictOfHashesMultiW
import operator
from string import digits
from os import listdir
from os.path import isfile, join
from collections import Counter
from nltk.stem import WordNetLemmatizer

hierarchy = dict()

def callMainCorpus(tweet):
	corpus_dict = dict()
	corpus_dict = dict_corpus.main()

	score_for_tweet = 0
	word_nr = -1

	for word in tweet:
		word_nr = word_nr + 1
		#word = lemmatizer.lemmatize(word)
		if word in corpus_dict:
			#print word
			#print corpus_dict[word]
			#print word + str(corpus_dict[word])
			score_for_word = corpus_dict[word]
		else:
			score_for_word = 0
		score_for_tweet = score_for_tweet + score_for_word
	#print "!!!!" + str(score_for_tweet) + "word_nr= " + str(word_nr)
	return score_for_tweet

def callCelebCorpus(tweet):
	celeb_dict = dict()
	celeb_dict = celeb_corpus.main()
	score_for_tweet = 0
	word_nr = -1

	for word in tweet:
		#print word
		if word in celeb_dict:
			#print word
			#print celeb_dict[word]
			print word + str(celeb_dict[word])
			score_for_word = celeb_dict[word]
		else:
			score_for_word = 0
		score_for_tweet = score_for_tweet + score_for_word
	return score_for_tweet

def callMultiCorpus(tweet):
	corpus_multi = dict()
	corpus_multi = dictOfHashesMultiW.main()
	score_for_tweet = 0
	for x in tweet:
		for y in tweet:
			if not x in y:
				line = x + " " + y
				if line in corpus_multi: 
					score_for_word = corpus_multi[line]
				else:
					score_for_word = 0
				score_for_tweet = score_for_tweet + score_for_word
	return score_for_tweet

def pprocTweet(tweet):
	tweet = tweet.lower()
	tweet = tweet.translate(None, string.punctuation)
	tweet = tweet.translate(None, digits)
	tweet = tweet.rstrip()
	words = tweet.split(" ")
	#for word in words:
		#print word

	return words

def rateTweets(tweet):
	#print "tweet: "+ str(tweet)
	lemmatizer = WordNetLemmatizer()
	corpus_dict = dict()
	corpus_dict = dict_corpus.main()

	celeb_dict = dict()
	celeb_dict = celeb_corpus.main()

	corpus_multi = dict()
	corpus_multi = dictOfHashesMultiW.main()

	score_for_tweet = 0
	word_nr = 0
	############ MAIN CORPUS ##############
	######score_for_tweet = score_for_tweet + callMainCorpus(tweet)
	word_nr = -1
	for word in tweet:
		word_nr = word_nr + 1
		#word = lemmatizer.lemmatize(word)
		if word in corpus_dict:
			#print word
			#print corpus_dict[word]
			#print word + str(corpus_dict[word])
			score_for_word = corpus_dict[word]
		else:
			score_for_word = 0
		score_for_tweet = score_for_tweet + score_for_word

	############ CELEB CORPUS ##############
	#######score_for_tweet = score_for_tweet + callCelebCorpus(tweet)
	for word in tweet:
		#print word
		if word in celeb_dict:
			#print word
			#print celeb_dict[word]
			#print word + str(celeb_dict[word])
			score_for_word = celeb_dict[word]
		else:
			score_for_word = 0
		score_for_tweet = score_for_tweet + score_for_word

	############ MULTI CORPUS ##############
	######score_for_tweet = score_for_tweet + callMultiCorpus(tweet)
	for x in tweet:
		for y in tweet:
			if not x in y:
				line = x + " " + y
				if line in corpus_multi: 
					score_for_word = corpus_multi[line]
				else:
					score_for_word = 0
				score_for_tweet = score_for_tweet + score_for_word

	#print "!!!!" + str(score_for_tweet) + "word_nr= " + str(word_nr)
	f = open('out.txt', 'w')
	f.write("score = " + str(score_for_tweet))
	f.write("\nnb of words = " + str(word_nr))
	print "score = " + str(score_for_tweet)
	print "nb of words = " + str(word_nr)
	f.close()
	norm_score = score_for_tweet / word_nr
	return norm_score
	#print "Score for this tweet is: " + str(score_for_tweet)

def readLinesFromFile(file):
	with open(file) as f:
		lines = f.readlines()
	fout = open('myfile.tsv','w')
	for line in lines:
		score = 0
		#print line
		pptweet = pprocTweet(line)
		#print pptweet
		score = rateTweets(pptweet)
		hierarchy[line] = score
		print line
		print "Score for this tweet is: " + str(score)

		 # python will convert \n to os.linese
		#fout.write("\nScore for this tweet is: " + str(score%2) + "\n")
		line = line +  str(score)


	#print lines

	#print hierarchy
	#sorted_hierarchy = sorted(hierarchy.items(), key=operator.itemgetter(1), reverse=True)
	#print sorted_hierarchy
	best_tweet = 1
	for k in sorted(hierarchy.items(), key=operator.itemgetter(1), reverse=True):
		info = 0
		for j in k:
			info = info + 1
			if info == 2:
				if best_tweet == 1:
					j = 2
				if best_tweet > 1 and best_tweet <= 10:
					j = 1
				if best_tweet > 10:
					j = 0 
				#print j
				score = j
			if info == 1:
				#print "tweet: " + j
				tweet = j
		myline = tweet.split()
		tweet_id = myline[0]
		print "$$$$$$$$$$$$$$$$     " + tweet_id + "  $$$$$$$$$$$$$$$$    "+str(score)
		line = tweet_id +"   " +str(score)
		line = line.replace('\n',"")

		fout.write(line + '\n')
		best_tweet = best_tweet + 1
	fout.close() # you can omit in most cases as the destructor will call it


def main(argv):
	pathFolder = sys.argv[1]
	run_type = sys.argv[2]
	print "Run type:" + run_type
	print pathFolder
	
	if run_type in "one":
		#tweet = raw_input('tweet =  ')
		#tweet = "Herein we have demonstrated a fundamental mechanical comparison between live cells and cells that were fixed with various concentrations of PFA AFM and SICM measurements showed that the apparent surface fluctuation amplitude and elastic modulus of cells underwent transition when exposed to PFA concentrations between  After complete PFA fixation cell surface fluctuation decreased to 71 of live cell while the Youngs modulus increased by fivefold compared to that of live cells These results provide a deeper understanding of how cells react to chemical treatment with PFA that takes into account not only the traditional chemical understanding of PFAs effect upon the cell but now also the cells surfacebased mechanical properties that were targeted in this study It is now apparent that PFA fixation enables the opening of distributed proteins across the cell surface a critical process that facilitates widespread crosslinking Cell membranes that are typically flexible and variable But in a certain situation, such as chemical treatment, biological functions are changed, and morphological changes also occur. This is the reason why studying cell surface fluctuations are crucial for the understanding of cell function about cell dynamics. Given the general nature of these physicochemical mechanisms, we expect that similar effects of PFA treatment on the elastic modulus and membrane fluctuations would also be expected although the specific magnitudes and responses conferred upon PFA treatment might vary on an absolute scale. We have confidence in that the SPM techniques could well serve as a promising tool for quantitative studies of both fixed cells and live cells in order to further explore this exciting topic at the convergence of biology and nanotechnology.\n"
		with open(pathFolder, 'r') as myfile:
			tweet=myfile.read().replace('\n', '')
		pptweet = pprocTweet(tweet)
		score = rateTweets(pptweet)

		print tweet
		print "Score - morm  for this tweet is: " + str(score)
		
		if score <= 1: 
			print "THE TONE FOR THIS PUB. IS --- GOOD-ENOUGHT !!!!!"
		if score > 1 and score <= 5:
			print "THE TONE FOR THIS PUB. IS --- AVERAGE!!!!!"
		if score >5: 
			print "THE TONE FOR THIS PUB. IS --- OUTSTANDING!!!!!"

	#f.write(str(score))  
	
	if run_type in "file":
		response = parser_for_train_data.main(pathFolder)
		onlyfiles = [f for f in listdir(pathFolder) if isfile(join(pathFolder, f))]
		for file in onlyfiles:
			fileName = pathFolder + "\\" + str(file)

		#fileName = "file.tsv"
		readLinesFromFile(fileName)

if __name__ == "__main__":
   main(sys.argv[1:])
