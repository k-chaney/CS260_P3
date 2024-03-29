#CS260-PA3-Problem1

#!/usr/bin/env python


class Dictionary:
	# Dictionary ADT implemented using an open hash table
	def __init__(self, buckets):
		self.table = [[]] * buckets

	def __getitem__(self, key):
		i = self.getHash(key)
		while len(self.table[i]) > 0:
			if self.table[i][0] == key:
				return self.table[i][1]
			else:
				i += 1
		print "Key cannot be found, deletion is successful"
		
	def getHash(self, x):
		return ord(x[0]) % len(self.table)
	
	def insert(self, key, value):
		i = self.getHash(key)
		count = 0
		while len(self.table[i]) > 0:
			if count > len(self.table):
				print "Hash table is full"
			i = i+1 if i < (len(self.table) - 1) else 0
			count += 1
		self.table[i] = [key, value]

	def delete(self, key):
		i = self.getHash(key)
		while len(self.table[i]) > 0:
			if self.table[i][0] == key:
				self.table[i] = []
				return True
			else:
				i += 1
		print "Key cannot be found"


if __name__ == '__main__':
	d = Dictionary(256)
	
	# Insert data
	print "\nInserting values"
	print "\n Insert 'Key1',which value is 3"
	print "\n Insert 'Key2',which value is 4"
	d.insert('Key1', '3')
	d.insert('Key2', '4')
	print "\nThe value of 'Key1' is :", d['Key1']
	
	# Delete data
	print "\nDeleting 'Key1' from dictionary\n"
	d.delete('Key1')
	try:
		print "The value of 'Key1' is :", d['Key1']
	except:
		print "Unable to find node; deletion successful"
		
	# Best case
	print "\nThe best numerical constant for insertion and deletion is 1. In the given example, it has only one value in the dictionary, so the average number of probes required to make either a deletion or an insertion is 1\n"
	


