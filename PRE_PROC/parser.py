import os
import sys
import glob, os


def main(argv):
	pathFolder = sys.argv[1]
	os.chdir(pathFolder)
	
	for file in glob.glob("*.xml"):
		with open(file) as fp:
			array = []
			for line in fp:
				array.append(line)
		f = open(file+'_out.txt', 'w')
		for index, item in enumerate(array):
			next = index + 1
			if next < len(array):
				if  "Conclusions" in item or "CONCLUSIONS" in item or "conclusions" in item:
					next = index + 1
					line = array[next].replace('<p>', '')
					line = line.replace('</p>', '')
					line = line.replace('<', '')
					line = line.replace('>', '')
					line = line.replace('"', '')
					line = line.replace('/', '')
					line = line.replace('\\', '')
					line = line.replace('=', '')
					line = line.replace('-', '')
					line = line.replace('(', '')
					line = line.replace(')', '')
					print line
					f.write(str(line))
				#if "Conclusions" in line:
					#print line

		#print array
if __name__ == "__main__":
   main(sys.argv[1:])