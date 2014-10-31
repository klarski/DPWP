'''
Kristen Kozinski
10/30/2014
Design Patterns for Web Programming
'''

madlib_answers = dict()

print "Fill in the following questions for a fun story."

#Answers for Madlib
madlib_answers['name']= raw_input('Enter a name:  ')
madlib_answers['gender'] = raw_input('Enter your gender (Male or Female):  ')
madlib_answers['age'] = raw_input('Enter your age: ')
madlib_answers['adjective1'] = raw_input('Enter an adjective: ')
madlib_answers['verb'] = raw_input('Enter a verb ending with ed: ')
madlib_answers['alcohol'] = []
madlib_answers['alcohol'].append(raw_input('Enter the name of an alcohol: '))
madlib_answers['alcohol'].append(raw_input('Enter the name of another alcohol: '))
madlib_answers['alcohol'].append(raw_input('Enter the name of yet another alcohol: '))
madlib_answers['booknumber'] = raw_input('Enter a number: ')
madlib_answers['celebrity'] = raw_input('Enter the name of a celebrity: ')
madlib_answers['animal_number'] = raw_input('Enter a number: ')
madlib_answers['animal'] = raw_input('Enter an animal: ')
madlib_answers['daynumber'] = raw_input('Enter a number: ')
madlib_answers['adjective2'] = raw_input('Enter an adjective: ')
madlib_answers['sports_team'] = raw_input('Choose a sports team: ')


#conditional for about sentence

about = ""

if madlib_answers['gender'] == "Male" and int(madlib_answers['age']) > 40:
    about = "I am a mature male looking for companionship."
elif madlib_answers['gender'] == "Male" and int(madlib_answers['age']) < 40:
    about = "I am a vivacious young fella and not looking for anything serious."
elif madlib_answers['gender'] == "Female" and int(madlib_answers['age']) > 40:
    about = "I am a experienced older woman who likes younger men."
else:
    about = "I am a independent career oriented woman looking for someone who can keep up with my active life"


#conditional statement that prints how many books you read and if you are smart
if madlib_answers['booknumber'] > 50:
    total_books = int(madlib_answers['booknumber'])*2
    total_books = (str(total_books) + ' books in my life so I am very smart.')
else:
    total_books = madlib_answers['booknumber']/2
    total_books = (str(total_books) + ' books in my life so I am not very bright.')

#function with loop inside of function the prints sports chant in personal ad
def sport_team():
    for i in range(1,3):
        print "Go " + madlib_answers['sports_team'] + " Go!"
        i = i + 1

#My personal Ad
print "My name is " + madlib_answers['name'] + ". " + about + " I enjoy long, " + madlib_answers['adjective1'] + " walks on the beach and getting " + madlib_answers['verb'] + " in the rain. I really like pina coladas mixed with " + madlib_answers['alcohol'][0] + ", " + madlib_answers['alcohol'][1] + ", " + madlib_answers['alcohol'][2] + ". I have read " + total_books + " My partner should have the physique of " + madlib_answers['celebrity'] + ". I would prefer if they knew how to cook, clean, and wash my " + madlib_answers['animal_number'] + " of " + madlib_answers['animal'] + ". I am also a huge " + madlib_answers['sports_team'] + " fan."
sport_team()
print " I know I am not very attractive in my picture, but it was taken " + madlib_answers['daynumber'] + " days ago and I have since become more " + madlib_answers['adjective2'] + "."
