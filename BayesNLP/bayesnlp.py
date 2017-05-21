	message = ("So if you could just go ahead and pack"
		"up your stuff and move it down there, that would be terrefic, OK?")

list_of_words = message.split()

dict_of_words = {}
for word in list_of_words:
	if word not in dict_of_words:
		dict_of_words[word] = 1
	else:
		dict_of_words[word] = dict_of_words[word] + 1

def prob(word):
	if word in dict_of_words:		
		return float(dict_of_words[word]) / float(len(list_of_words))
	else:
		return 0

print message
# print list_of_words
print dict_of_words

print "Probability of 'if' %f" % prob('if') 
print "Probability of 'you' %f" % prob('you') 



