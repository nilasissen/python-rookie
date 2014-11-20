#pirate language convertor :D
import urllib

def convert_word():
        word = raw_input('enter ur word----->   ')
        connection = urllib.urlopen("http://isithackday.com/arrpi.php?text="+word)
        output = connection.read()
        print(output)
convert_word()
                            
                            
                            
   
