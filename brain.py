import turtle              #importing the turtle from standard lib
    
def draw_square(turtle,length):       #drawing square module 
     """this program will draw a pattern"""
     for i in range (4):
           turtle.forward(length)            #turtle.forward is use to move the pointer forward
           turtle.right(90)
        
        
                   
     
             
                    
def draw_circle(turtle,radius):           #drawing circle 
     for i in range(1):               
         turtle.circle(radius)
                   
              
def main():
          brad = turtle.Turtle()            #creating an instance brad for turtle
          brad.shape("turtle")          # we can design the pointer for eg:color shape,speed
          brad.color("red")
          brad.speed(8)
          for i in range(40):
              
              draw_square(brad,100)
              draw_circle(brad,100)
              brad.right(10)
main()
            
             

            
    
          


           


       
             
    


    
   
    
            
            
       
        

  
   
   
         

          
           

            
           
            

               
