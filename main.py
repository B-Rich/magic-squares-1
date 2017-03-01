import time
import random
import os, sys
import copy

t0 = time.time()
f = open('dictionary.txt', 'r')
lines = f.readlines()
f.close()
t1 = time.time()

print 'time to readlines: ', (str( t1 - t0)[:5])
print 'number of lines: ', len(lines)
print '\n'
for i in range(5):
    r = random.randint(0,len(lines))
    print 'word #', str(r), ' : ', str(lines[r])


t0 = time.time()
words = []
for line in lines:
    strip_line = line.rstrip("\n")
    words.append(strip_line)
t1= time.time()

print 'len of words: ', str(len(words))
print 'time to create list : ', str(t1-t0)[:5]

print "FALSE: lines[0]=='AA': ", str(lines[0]=='AA')
print "TRUE: lines[0]=='AA\n': ", str(lines[0]=='AA\n')
print "TRUE: words[0]=='AA': ", str(words[0]=='AA')

def n_letter_words(n, input, **kwargs):
    return filter(lambda w: len(w) == n, input)

for _n in range(1,20):
    
    n_letters = n_letter_words(_n, words)
    print "n=",str(_n), ": ", str(len(n_letters))    
    
    if len(n_letters) > 0:
        out = n_letters[:min(4, len(n_letters))]
        print ("\n").join(out)

def search_me(_w, words):
    return filter(lambda w: w ==_w, words)


for this_word in ["AA", "ITALIAN", "ENGLISH", "PHALLIC", "ABACUS", "ITALY", "ENGLAND"]:
    print this_word, " - ", str(search_me(this_word, words))


print 'done'


def search_word(N,**kwargs):
    r = random.randint()
    return 

def satisfy(lwords,inds):
    
    for iword ,word in enumerate(lwords):
        
        if not( iword in inds): continue
        
        for iletter, letter in enumerate(word):
 
            if not(iletter in ind): continue
            if (letter != lwords[iletter][ iletter]):
                return False

    return True

good = ["WILL", "ICEY", "LEAN", "LYNX"]
print satisfy(good, range(4))

good_kinda = ["WILL", "", "LEAN", "LYNX"]
print satisfy(good_kinda, [0,2,3])

good_kinda2 = ["WILL", "JJJJ", "LEAN", "LYNX"]
print satisfy(good_kinda, [0,2,3])

print 'SAD!'
good_kinda2 = ["WILL", "JJJJ", "LEAN", "LYNX"]
print satisfy(good_kinda, [0,1,2,3])

    


































































