import turtle

t = turtle.Turtle()
t.speed(10)

def draw(size, depth):
  if depth == 0:
    t.forward(size)
    return
  
  draw(size / 3, depth - 1)
  t.left(60)
  draw(size / 3, depth - 1)
  t.right(120)
  draw(size / 3, depth - 1)
  t.left(60)
  draw(size / 3, depth - 1)
    
    
    
draw(200,2)
