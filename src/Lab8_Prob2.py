'''
Created on Mar 21, 2017

@author: Chris Gick 
'''

encryptCode = {'A': '~', 'a': '`',\
               'B': '!', 'b': '1',\
               'C': '@', 'c': '2',\
               'D': '#', 'd': '3',\
               'E': '$', 'e': '4',\
               'F': '%', 'f': '5',\
               'G': '^', 'g': '6',\
               'H': '&', 'h': '7',\
               'I': '*', 'i': '8',\
               'J': '(', 'j': '9',\
               'K': ')', 'k': '0',\
               'L': '_', 'l': '-',\
               'M': '+', 'm': '=',\
               'N': '{', 'n': '[',\
               'O': '}', 'o': ']',\
               'P': '|', 'p': '\\',\
               'Q': ':', 'q': ';',\
               'R': '"', 'r': '\'',\
               'S': '<', 's': ',',\
               'T': '>', 't': '.',\
               'U': '?', 'u': '/',\
               'V': 'A', 'v': 'a',\
               'W': 'B', 'w': 'b',\
               'X': 'C', 'x': 'c',\
               'Y': 'D', 'y': 'd',\
               'Z': 'E', 'z': 'e',\
               '1': 'F', '2': 'f',\
               '3': 'G', '4': 'g',\
               '5': 'H', '6': 'h',\
               '7': 'I', '8': 'i',\
               '9': 'J', '0': 'j',\
               '.': 'K', ',': 'k',\
               ';': 'L', ':': 'l',\
               '!': 'M', '@': 'm',\
               '#': 'N', '$': 'n',\
               '%': 'O', '&': 'o',\
               '?': 'P', '*': 'p',\
               '-': 'Q', '+': 'q',\
               '/': 'R', '\\': 'r',\
               '"': 'S', '\'': 's',\
               '_': 'T', '=': 't',\
               '(': 'U', ')': 'u',\
               '{': 'V', '}': 'v',\
               '[': 'W', ']': 'w',\
               '^': 'X', '|': 'x',\
               '<': 'Y', '>': 'y',\
               '`': 'Z', '~': 'z',\
               }

def main():
    print('main start')
    try:
        #open Files 
        inFile = open(r'..\data\inputText.txt', 'r')
        outFile = open(r'..\data\outText.txt', 'w')
        
        #loop through each line in the file
        for l in inFile:
            #create a var to hold the encoded line
            encoded = ''
            
            #loop through each charater in the line
            for c in l.rstrip('\n'):
                
                #if its a space add it to the encoded line
                if c == "'":
                    encoded += encryptCode['\'']
                    
                if c.isspace():
                    encoded += c
                
                #look up the encoded value in the dictionary and add 
                #it to the encoded line
                else:
                    encoded += encryptCode[c]
                    
            #Write the encoded line to the output file
            outFile.write(encoded)
            
        #close files
        inFile.close()
        outFile.close()
        
        print('program end')
    except Exception as err:
        print('Error: ' + str(err))
        
main()