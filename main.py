#! /bin/env python3
import turtle as t
import json
config = json.load(open("./config.json","r"))
t.setup(width=0.75, height=0.75, startx=None, starty=None)
t.hideturtle()
t.delay(0)
t.tracer(n=10000)
# config init
size =  {"h":140,"w":250}
ruleType = 93

map = []
result = []
for i in range(size["h"]):
  map.append([])
  result.append([])
  for j in range(size["w"]):
    map[i].append(0)
    result[i].append(0)
map[0][size["w"]//2] = 1
result[0][size["w"]//2] = 1
#types
types=[(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]
texts=[" ","@"]

#setRule
ruleType = int(ruleType)
if not (ruleType >= 0 and ruleType <= 255):
 raise ValueError("Invalid ruleType number")
ruleTypeBin = format(ruleType,"b")
ruleTypeBin = "0"*(8-len(ruleTypeBin)) + ruleTypeBin
black = []
white = []
for i in range(len(ruleTypeBin)):
  if ruleTypeBin[i] == "1":
    black.append(types[i])
  else:
    white.append(types[i])

# define functions
def getColor(h,w):
  if w == 0:
    data = (map[h-1][-1],map[h-1][w],map[h-1][w+1])
  elif w == size["w"]-1:
    data = (map[h-1][w-1],map[h-1][w],map[h-1][0])
  else:
    data = (map[h-1][w-1],map[h-1][w],map[h-1][w+1])
  for i in black:
    if i[0] == data[0] and i[1] == data[1] and i[2] == data[2]:
      return 1
  return 0
def getTurtlePos(h,w):
  x = (w - size["w"]//2) * 4 - 2
  y = h * (-4) + 320
  return (x,y)
def fillTurtle(pos1,pos2):
  if pos1[0] > pos2[0]:
    x = (pos2[0],pos1[1])
    y = (pos1[0],pos2[1])
    fillTurtle(x,y)
  elif pos1[1] > pos2[1]:
    x = (pos1[0],pos2[1])
    y = (pos2[0],pos2[1])
    fillTurtle(x,y)
  else:
    t.up()
    t.goto(pos1[0],pos1[1])
    t.down()
    for i in range(int(pos2[0] - pos1[0] + 1)):
      t.goto(t.xcor(),pos2[1])
      t.goto(t.xcor()+1,pos1[1])
    t.goto(t.xcor(),pos2[1])
  t.up()
t.up()
t.seth(90)
t.goto(-2,320)
def paintSquare():
  t.down()
  for i in range(4):
    t.right(90)
    t.forward(4)
  t.up()
paintSquare()
fillTurtle((-2,316),(2,320))
t.up()
text = ""
for i in map[0]:
  text+=texts[i]
for h in range(1,size["h"]):
  print(text)
  text = ""
  for w in range(size["w"]):
    map[h][w] = getColor(h,w)
    text += texts[getColor(h,w)]
    t.up()
    if map[h][w] == 1:
      t.goto(getTurtlePos(h,w)[0],getTurtlePos(h,w)[1])
      paintSquare()
      fillTurtle((getTurtlePos(h,w)[0],getTurtlePos(h,w)[1]-4),(getTurtlePos(h,w)[0]+4,getTurtlePos(h,w)[1]))
print(text)

print("Rule Set:")
print("Black:",black)
print("White:",white)
t.mainloop()
