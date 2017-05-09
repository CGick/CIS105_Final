'''
Created on Mar 21, 2017

@author: Chris Gick
'''
#Global Constant    
courseRoom = {'CS101': '3004',\
               'CS102': '4501',\
               'CS103': '6755',\
               'NT110': '1244',\
               'CM241': '1411'}

courseInstructor = {'CS101': 'Haynes',\
                    'CS102': 'Alvarado',\
                    'CS103': 'Rich',\
                    'NT110': 'Burke',\
                    'CM241': 'Lee'}

courseTime = {'CS101': '8:00 a.m.',\
              'CS102': '9:00 a.m.',\
              'CS103': '10:00 a.m.',\
              'NT110': '11:00 a.m.',\
              'CM241': '1:00 p.m.'}

'''
main method

@summary: displays a list of courses then prompts user for a course then displays the 
room number, time of meeting, and instructor teaching the course
'''
def main():
    courses = courseInstructor.keys()
    print("The courses we offer are: ")
    for i in courses:
        print(i)
        
    course = input('Enter a course: ')
    print("Your course meets in room " + courseRoom[course.upper()] +\
          ' at ' + courseTime[course.upper()] +\
          ', and your instructor will be Professor ' + courseInstructor[course.upper()] + '.')


#run main
main()