import turtle
t = turtle.Turtle()
t.speed(2)
t.left(90)

def draw_tree(size, angle, current):
  if current <= 10:
    return
  
  t.forward(current)
  t.right(angle / 2)
  draw_tree(size, angle, current - 12)
  t.left(angle)
  draw_tree(size, angle, current - 12)
  t.right(angle / 2)
  t.backward(current)
  
def tree(size, angle):
  draw_tree(size, angle, size)
  
tree(100, 60)
