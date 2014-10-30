'''
Kristen Kozinski
10/30/2014
Design Patterns for Web Programming
'''

madlib_answers = dict()

#madlib_answers['name']= raw_input('Enter a name:  ')
#madlib_answers['adjective1'] = raw_input('Enter an adjective: ')
#madlib_answers['verb'] = raw_input('Enter a verb ending with ed: ')
#madlib_answers['alcohol'] = raw_input('Enter the name of an alcohol: ')
#madlib_answers['alcohol'] = raw_input('Enter the name of another alcohol: ')
#madlib_answers['alcohol'] = raw_input('Enter the name of yet another alcohol: ')
madlib_answers['booknumber'] = raw_input('Enter a number: ')
#madlib_answers['celebrity'] = raw_input('Enter the name of a celebrity: ')
#madlib_answers['animal_number'] = raw_input('Enter a number: ')
#madlib_answers['animal'] = raw_input('Enter an animal: ')
#madlib_answers['daynumber'] = raw_input('Enter a number: ')
#madlib_answers['adjective2'] = raw_input('Enter an adjective: ')

if madlib_answers['booknumber'] > 50:
    total_books = int(madlib_answers['booknumber'])*2
    total_books = (str(total_books) + ' books in my life so I am very smart.')
else:
    total_books = madlib_answers['booknumber']/2
    total_books = (str(total_books) + ' books in my life so I am not very bright.')
