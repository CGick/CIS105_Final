'''
Created on Mar 25, 2017

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

def display_decode_file():
    try:
        #open files
        decodeFileIn = open(r'..\data\encodeFileOut.txt', 'r')
        
        #loop through input file
        for l in decodeFileIn:
            #var for holding decoded line
            decode = ''
            
            #loop through each character in the line
            for c in l.rstrip('\n'):
                #test if character is a space
                if c.isspace():
                    decode += c
                else:
                    #loop through each key value pair in encryptCode
                    for key, val in encryptCode.items():
                        #check if the character is in the dictionary 
                        #and write it's key to the decoded line
                        if c == val:
                            decode += key
                            break
            #print decoded line to output
            print(decode)  
        
        #close file
        decodeFileIn.close()
                            
    except Exception as err:
        print('Error: ' + str(err))
    
def main():
    print('<program start>')
    display_decode_file()
    print('<program end>')
    
main()