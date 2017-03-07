import os, sys, random, time
PATH = "data/en-us/hunspell/en_us.dic"

class BigWords:    

    @staticmethod
    def get_dictionary():
        t0 = time.time()
        f = open(PATH, 'r')
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
            
            strip_line = line.split('/')[0]
            strip_line = strip_line.rstrip("\n")
            final = strip_line.upper()
            words.append(final)

        t1= time.time()
        print 'time to processlines: ', (str( t1 - t0)[:5])

        return words

    #words = get_dictionary()

    #print 'len of words: ', str(len(words))

    


