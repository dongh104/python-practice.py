import turtle
t=turtle.Turtle()
t.shape("turtle")
side = 50 
angle = 90  
for a in range(4): 
   for b in range(3): 
      t.forward(side) 
      t.left(angle) 
   t.forward(side)
