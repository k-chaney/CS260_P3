# CS260-PA3-Problem 4

#!/usr/bin/env python


from array import *
from list_array import *
import sys

def makeTrie():
    
    # create empty array
	Words = []
    
    #read Alice in Wonderland
	fileName = raw_input("\nPlease enter the file name you want to open:")
	f = open(str(fileName),"r");
	lines = f.readlines();
    
	for i in lines:
		thisline = i.split(" ");	
		for j in thisline:
			if j!="":
				Words.append(j.strip())

	x=ListArray()

	for word in Words:
		for letter in word:
			if (word!=""):
				x.insert(letter,x.end())
		x.insert("$",x.end())

	count=0
	counter=0


	while(x.retrieve(counter)!=None):
		if x.retrieve(counter)=="$":
			count=count+1
		counter=counter+1
	return count


print "\nThe program creats an array list which contains all the words that are in Alice in Wonderland.\n"

print "Then it iterates through each word, and adds the corresponding letters in order to the list_array implementation.\n"

print "The letters following each letter are stored in a lst. There is a '$' inserted after the end of each word. So the number of occurences of '$' is same as the size of the trie.\n"

print "The size of the trie of Alice In Wonderland is:",makeTrie(),".\n"


