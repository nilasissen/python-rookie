import turtle
    
def draw_square(turtle,length):
     """this program will draw a pattern"""
     for i in range (4):
           turtle.forward(length)
           turtle.right(90)
        
        
                   
     
             
                    
def draw_circle(turtle,radius):
     for i in range(1):
         turtle.circle(radius)
                   
              
def main():
          brad = turtle.Turtle()
          brad.shape("turtle")
          brad.color("red")
          brad.speed(8)
          for i in range(40):
              
              draw_square(brad,100)
              draw_circle(brad,100)
              brad.right(10)
main()
            
             

            
    
          


           


       
             
    


    
   
    
            
            
       
        

  
   
   
         

          
           

            
           
            

               
