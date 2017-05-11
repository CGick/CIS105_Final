'''
Created on Mar 25, 2017

@author: Chris Gick
'''
#imports
import pickle

#menu options
SHOW_LIST = 1
LOOK_UP =2
ADD = 3
CHANGE = 4
DELETE = 5
QUIT = 6

def main():
    #get email list form file
    emails = {}
    
    #sentinal flag for loop control
    choice = 0
    
    #loop to continue program as long as user wants to
    while choice != 6:
        #prompt user for menu Option
        choice =  get_option()
        
        #process choice
        if choice == SHOW_LIST:
            show_list(emails)
        elif choice == LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            add(emails)
        elif choice == CHANGE:
            change(emails)
        elif choice == DELETE:
            delete(emails)
    #send email list to file 
    store_email_list(emails)
    
def get_option():
    #display menu options
    print('Email list') 
    print('____________________________________')
    print('1. Show list of email addresses.')
    print('2. Look up an email address.')
    print('3. Add an email address.')
    print('4. Change an existing email address.')
    print('5. Delete an existing email address.')
    print('6. Quit program.')
    print()
    
    
    try:
        #get user input
        c = int(input('Enter menu choice: '))
        
        #validation loop
        while c < SHOW_LIST or c > QUIT:
            c = int(input('Please enter a menu option: '))
            
    #handles a non numeric keyboard input
    except ValueError:
        c = 0
        while c < SHOW_LIST or c > QUIT:
            c = int(input('Please enter a numeric menu option: '))
            
    return c

def show_list(dictionary):
    #loop through each dictionary item and display
    for ky, val in dictionary.items():
        print(ky, val)
    print()
        
def look_up(dictionary):
    #get name
    nm = input('Enter a name: ')
    
    #display email
    print(dictionary.get(nm, 'That person is not in your email list.'))
    print()
    
def add(dictionary):
    #get name and email
    nm = input('Enter a name: ')
    mail = input('Enter an email for that person: ')
    
    #if entry not in email list add it
    if nm not in dictionary:
        dictionary[nm] = mail
    else:
        print(nm + ' is already in your email list.')
    print()
        
def change(dictionary):
    #get name
    nm = input('Enter a name: ')
    
    #if entry in email list change email for entry 
    if nm in dictionary:
        mail = input('Enter a new email address for ' + nm + ': ')
        
        dictionary[nm] = mail
    else:
        print(nm + ' does not exist in your email list.')
    print()
      
def delete(dictionary):
    nm = input('Enter a name: ')
    
    #if entry in email list delete it
    if nm in dictionary:
        #verify request for deletion
        print('Are you sure you want to delete ' + nm + ' from your email list?')
        opt = input('Yes or No: ')
        if opt[0].lower() == 'y':
            del dictionary[nm]
            print(nm + ' has been delete.')
    else:
        print(nm + ' is not in your email list.')
    print()
def store_email_list(dictionary):
    try:
        #open file
        file = open(r'..\data\emailList.dat', 'wb')
        
        #write serialized email list to file
        pickle.dump(dictionary, file)
        
        #close file
        file.close()
    except IOError as err:
        print('Error: ' + str(err))    
#run main
main()