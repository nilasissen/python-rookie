import time           #importing the time
import webbrowser   #importing the web browser 
total_break=3
flag=0
print ("this program started at"+time.ctime()) #to know whn the program runs, the function is for current time
while(flag<=total_break):
    #while loop to repeat the program
    time.sleep(2*60*60)         #making the program w8 for 10 sec
    webbrowser.open("https://www.youtube.com/watch?v=mIQToVqDMb8")#opening the web browser
    flag=flag+1
"""this program is use full for those who site for long time in computer.This simple program is use for alarm clock .after every 2 hours of time it will open the browser 
and it will play the fav song of the programer"""