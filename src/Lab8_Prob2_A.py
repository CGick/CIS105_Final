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


def encode_file():
    
    try:
        #open Files
        encodeFileIn = open(r'..\data\encodeFilein.txt', 'r')
        encodeFileOut = open(r'..\data\encodeFileOut.txt', 'w')
        
        #loop through each line in the file
        for l in encodeFileIn:
            #create a var to hold the encoded line
            encoded = ''
            #loop through each charater in the line
            for c in l.rstrip('\n'):
                #if its a space add it to the encoded line
                if c.isspace():
                    encoded += c
                else:
                    encoded += encryptCode[c]
            
            #Write the encoded line to the output file
            #look up the encoded value in the dictionary and add
            #it to the encoded line
            encodeFileOut.write(encoded + '\n')

        #close files
        encodeFileIn.close()
        encodeFileOut.close()
         
    except Exception as err:
        print('Error: ' + str(err))
    
def decode_file():
    try:
        #open files
        decodeFileIn = open(r'..\data\encodeFileOut.txt', 'r')
        decodeFileOut = open(r'..\data\decodeFileOut.txt', 'w')
        
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
                        
            #write decoded line to file
            decodeFileOut.write(decode + '\n')   
        
        #close files
        decodeFileIn.close()
        decodeFileOut.close()
                            
    except Exception as err:
        print('Error: ' + str(err))
    
def main():
    print('<program start>')
    encode_file()
    decode_file()
    print('<program end>')

main()