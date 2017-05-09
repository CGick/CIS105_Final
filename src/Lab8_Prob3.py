'''
Created on Mar 25, 2017

@author: Chris Gick    
'''


def get_sets():
    try:
        #open files
        file1 = open(r'..\data\compFile1.txt', 'r')
        file2 = open(r'..\data\compFile2.txt', 'r')
        
        #var to hold strings
        conFile1 = ''
        conFile2 = ''
        
        #loop through file to get content
        for l in file1:
            conFile1 += l.rstrip('\n').lower().replace('.', '')
        for l in file2:
            conFile2 += l.rstrip('\n').lower().replace('.', '')
        
        #create sets
        wordset1 = set(conFile1.split(' '))
        wordset2 = set(conFile2.split(' '))
        
        #close files
        file1.close()
        file2.close() 
    except Exception as err:
        print('Error: ' + str(err))
    
    #return sets
    return wordset1, wordset2

def format_print(wrd, cnt):
    #indents the first word of each line
    if cnt == 0:
        print('    ', wrd, end=' ')
        cnt+= 1  
    #creates a new line after 8 words
    elif cnt == 7:
        print()
        cnt = 0
    else:
        print(wrd, end=' ')
        cnt += 1
    return cnt
    
def main():
    #get sets
    set1, set2 = get_sets()
        
    print('All of the unique words in both files are:')
    c = 0
    #loops through each word in the union of both sets
    for w in set1 | set2:
        c = format_print(w, c)
        
    print('The words that are in both files are: ')
    c = 0
    for w in set1 & set2:
        c = format_print(w, c)
    print()
    print('The words that appear in file 1 but not file 2 are:')
    c = 0
    for w in set1 - set2:
        c= format_print(w, c)
    print()
    print('The words that appear in file 2 but not file 1 are:')
    c = 0
    for w in set2 - set1:
        c = format_print(w, c)
    print()
    print('The words that appear in file 1 or file 2 but not both are:')
    c = 0
    for w in set1 ^ set2:
        c = format_print(w, c)
main()