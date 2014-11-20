#!/usr/local/bin/python
print 'Legal age in INDIA'
driving_age=16
voting_age=18
smoking_age=19
marriage_age=21
age = int(raw_input('enter your age :) '))
def   get_age(age):
    """this program will teach you about the if and else and elif statements """
    if age >= marriage_age:
        print 'you can get marriad,smoke,vote,and drive '
    elif age >= smoking_age:
        print 'you cant smoke,vote,drive '
    elif age >= voting_age:
        print 'you can only vote and driving '
    elif age >= drive_age:
       print 'you can driving '
    else:
       print 'you cant even vote'
        
		
		

