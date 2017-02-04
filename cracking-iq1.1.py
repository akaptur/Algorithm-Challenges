#
# Cracking the Coding Interview - Interview Question 1.1
# Justin Haaheim
#

# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

test_input_1 = "abcdefgc"
test_input_2 = "jklmnopqrs"

# clarifications to ask: capitalization matters? what character set are we using?
# simple solution: use a hash table

def is_unique(input_string):
	
	char_count = dict()
	
	for char in input_string:
		if char_count.has_key(ord(char)):
			char_count[ord(char)] += 1
			if char_count[ord(char)] > 1:
				return False
		else:
			char_count[ord(char)] = 1
			
	# at this point, we've processed through the whole string, and there hasn't been more than one of any character. return true
	return True
	
print "Is {0} unique? {1}".format(test_input_1, is_unique(test_input_1))
print "Is " + test_input_2 + " unique? ", str(is_unique(test_input_2))


		