import turtle

t = turtle.Turtle()
t.speed(5)

def draw(angle, size, step):
  if step == 1:
    t.right(angle)
   
  t.forward(size)
  t.right(90)
  
  if size <= 0:
    return
  
  if step == 4:
    t.forward(size / 15)
    return draw(angle + 2, size - 15, 1)
  
  return draw(angle, size, step + 1)
  	

def main():
	draw(0, 200, 1)
  
main()
