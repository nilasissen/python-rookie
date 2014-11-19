import urllib

def bad_word():
    """ ==NS==
This program is use to check if any curse word is present in the document .this is one of the easy program which will teach you about how to read line from 
a document """

"""The link "http://www.wdyl.com/profanity?q=" is a google website which can take an input line and will tell if any curse word is present in the line"""
#module

    file = open(r"C:\Python27\python\badword.txt") #opening a file from particular location 
    contents_of_file = file.read()                #reading line from the file 
    print(contents_of_file)
    file.close()                                  #closing the file
    check_bad(contents_of_file)          #calling check_bad module to check for any bad word
def check_bad(text_to_check):
   connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check) #opening connection 
   output = connection.read()           #text_to_check is the input line from the user
   print(output)                        #you can check the output of u want
   connection.close()					#closing the connection 
if "true" in output:
    print("this doc has bad words in it")
elif "false" in output:
     print("this doc dsnt have any bad word in it")
else:
     print("houston we have a problem the input is wrong")
       
   
bad_word()
                
