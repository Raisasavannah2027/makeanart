import turtle
import random
import time
# The higher ↓this integer is, the faster the drawing.



# # First Test (Testing the radomiser)
# for i in range(50):
#   x = random.randint(1 ,360)
#   y = random.randint(1 ,80)
#   turtle.forward(y)
#   turtle.right(x)

# # Second Test (Genorating a radom shape)
# x = random.randint(90 ,360)
# y = random.randint(30 ,90)
# z = random.randint(50 ,300)
# for i in range(z):
#   turtle.forward(y)
#   turtle.right(x)
# # p = turtle.pos()
# # if p == (0 ,0):
# #   break


def randomcolor():
  randcolorlist = ['maroon', 'darkred',	'brown', 'firebrick', 'crimson', 'red', 'tomato', 'coral', 'indianred', 'lightcoral', 'darksalmon', 'salmon', 'lightsalmon', 'orangered', 'darkorange',	'orange', 'gold', 'darkgoldenrod', 'goldenrod', 'palegoldenrod', 'darkkhaki', 'khaki', 'olive', 'yellow', 'yellowgreen', 'darkolivegreen', 'olivedrab', 'lawngreen', 'chartreuse',	'greenyellow','darkgreen', 'green', 'forestgreen', 'lime', 'limegreen', 'lightgreen', 'palegreen', 'darkseagreen', 'mediumspringgreen', 'springgreen', 'seagreen', 'mediumaquamarine', 'mediumseagreen', 'lightseagreen', 'darkslategray', 'teal', 'darkcyan', 'aqua', 'cyan',	'lightcyan', 'darkturquoise', 'turquoise', 'mediumturquoise', 'paleturquoise', 'aquamarine', 'powderblue', 'cadetblue', 'steelblue', 'cornflowerblue',	'deepskyblue', 'dodgerblue', 'lightblue', 'skyblue', 'lightskyblue',	'midnightblue', 'navy', 'darkblue', 'mediumblue', 'blue', 'royalblue', 'blueviole', 'indigo', 'darkslateblue', 'slateblue', 'mediumslateblue', 'mediumpurple', 'darkmagenta', 'darkviolet', 'darkorchid', 'mediumorchid',	'purple', 'thistle', 'plum', 'violet',	'magenta', 'orchid', 'mediumvioletred', 'palevioletred', 'deeppin', 'hotpink', 'lightpink',	'pink', 'antiquewhite', 'beige', 'bisque',	'blanchedalmond',	'wheat', 'cornsilk',	'lemonchiffon', 'lightgoldenrodyellow', 'lightyellow', 'saddlebrown', 'sienna', 'chocolate', 'peru', 'sandybrown', 'burlywood', 'tan', 'rosybrown', 'moccasin', 'navajowhite', 'peachpuff', 'mistyrose', 'lavenderblush', 'linen', 'oldlace', 'papayawhip', 'seashell', 'mintcream', 'slategray', 'lightslategray', 'lightsteelblue', 'lavender', 'floralwhite', 'aliceblue', 'ghostwhite', 'honeydew', 'ivory', 'azure', 'snow', 'black', 'dimgray', 'gray', 'darkgray', 'silver', 'lightgray', 'gainsboro', 'whitesmoke', 'white']
  r = random.choice(randcolorlist)
  return(r)

maroon = (128,0,0)
darkred = (139,0,0)
brown = (165,42,42)
firebrick = (178,34,34)
crimson = (220,20,60)
red = (255,0,0)
tomato = (255,99,71)
coral = (255,127,80)
indianred = (205,92,92)
lightcoral = (240,128,128)
darksalmon = (233,150,122)
salmon = (250,128,114)
lightsalmon = (255,160,122)
orangered = (255,69,0)
darkorange = (255,140,0)
orange = (255,165,0)
gold = (255,215,0)
darkgoldenrod = (184,134,11)
goldenrod = (218,165,32)
palegoldenrod = (238,232,170)
darkkhaki = (189,183,107)
khaki = (240,230,140)
olive = (128,128,0)
yellow = (255,255,0)
yellowgreen = (154,205,50)
darkolivegreen = (85,107,47)
olivedrab = (107,142,35)
lawngreen = (124,252,0)
chartreuse = (127,255,0)
greenyellow = (173,255,47)
darkgreen = (0,100,0)
green = (0,128,0)
forestgreen = (34,139,34)
lime = (0,255,0)
limegreen = (50,205,50)
lightgreen = (144,238,144)
palegreen = (152,251,152)
darkseagreen = (143,188,143)
mediumspringgreen = (0,250,154)
springgreen = (0,255,127)
seagreen = (46,139,87)
mediumaquamarine = (102,205,170)
mediumseagreen = (60,179,113)
lightseagreen = (32,178,170)
darkslategray = (47,79,79)
teal = (0,128,128)
darkcyan = (0,139,139)
aqua = (0,255,255)
cyan = (0,255,255)
lightcyan = (224,255,255)
darkturquoise = (0,206,209)
turquoise = (64,224,208)
mediumturquoise = (72,209,204)
paleturquoise = (175,238,238)
aquamarine = (127,255,212)
powderblue = (176,224,230)
cadetblue = (95,158,160)
steelblue = (70,130,180)
cornflowerblue = (100,149,237)
deepskyblue = (0,191,255)
dodgerblue = (30,144,255)
lightblue = (173,216,230)
skyblue = (135,206,235)
lightskyblue = (135,206,250)
midnightblue = (25,25,112)
navy = (0,0,128)
darkblue = (0,0,139)
mediumblue = (0,0,205)
blue = (0,0,255)
royalblue = (65,105,225)
blueviolet = (138,43,226)
indigo = (75,0,130)
darkslateblue = (72,61,139)
slateblue = (106,90,205)
mediumslateblue = (123,104,238)
mediumpurple = (147,112,219)
darkmagenta = (139,0,139)
darkviolet = (148,0,211)
darkorchid = (153,50,204)
mediumorchid = (186,85,211)
purple = (128,0,128)
thistle = (216,191,216)
plum = (221,160,221)
violet = (238,130,238)
magenta = (255,0,255)
orchid = (218,112,214)
mediumvioletred = (199,21,133)
palevioletred = (219,112,147)
deeppink = (255,20,147)
hotpink = (255,105,180)
lightpink = (255,182,193)
pink = (255,192,203)
antiquewhite = (250,235,215)
beige = (245,245,220)
bisque = (255,228,196)
blanchedalmond = (255,235,205)
wheat = (245,222,179)
cornsilk = (255,248,220)
lemonchiffon = (255,250,205)
lightgoldenrodyellow = (250,250,210)
lightyellow = (255,255,224)
saddlebrown = (139,69,19)
sienna = (160,82,45)
chocolate = (210,105,30)
peru = (205,133,63)
sandybrown = (244,164,96)
burlywood = (222,184,135)
tan = (210,180,140)
rosybrown = (188,143,143)
moccasin = (255,228,181)
navajowhite = (255,222,173)
peachpuff = (255,218,185)
mistyrose = (255,228,225)
lavenderblush = (255,240,245)
linen = (250,240,230)
oldlace = (253,245,230)
papayawhip = (255,239,213)
seashell = (255,245,238)
mintcream = (245,255,250)
slategray = (112,128,144)
lightslategray = (119,136,153)
lightsteelblue = (176,196,222)
lavender = (230,230,250)
floralwhite = (255,250,240)
aliceblue = (240,248,255)
ghostwhite = (248,248,255)
honeydew = (240,255,240)
ivory = (255,255,240)
azure = (240,255,255)
snow = (255,250,250)
black = (0,0,0)
dimgray = (105,105,105)
gray = (128,128,128)
darkgray = (169,169,169)
silver = (192,192,192)
lightgray = (211,211,211)
gainsboro = (220,220,220)
whitesmoke = (245,245,245)
white = (255,255,255)
  
p1 = randomcolor()
print(p1)

p2 = randomcolor()
print(p2)

p3 = randomcolor()
print(p3)

p4 = randomcolor()
print(p4)

p5 = randomcolor()
print(p5)

p6 = randomcolor()
print(p6)

p7 = randomcolor()
print(p7)

# print(p)

t1 = turtle.Turtle()
t1.shape("turtle")
t1.speed(7)
t1.color('black')
t1.fillcolor(p1)
t1.begin_fill()
# t1.hideturtle()

t2 = turtle.Turtle()
t2.shape("turtle")
t2.speed(7)
t2.color('black')
t2.fillcolor(p2)
# t2.hideturtle()

t3 = turtle.Turtle()
t3.shape("turtle")
t3.speed(7)
t3.color('black')
t3.fillcolor(p3)
# t3.hideturtle()

t4 = turtle.Turtle()
t4.shape("turtle")
t4.speed(7)
t4.color('black')
t4.fillcolor(p4)
# t4.hideturtle()

t5 = turtle.Turtle()
t5.shape("turtle")
t5.speed(7)
t5.color('black')
t5.fillcolor(p5)
# t5.hideturtle()

t6 = turtle.Turtle()
t6.shape("turtle")
t6.speed(7)
t6.color('black')
t6.fillcolor(p6)
# t6.hideturtle()

t7 = turtle.Turtle()
t7.shape("turtle")
t7.speed(7)
t7.color('black')
t7.fillcolor(p7)
# t7.hideturtle()

# ('black')

# # # # A Star of Daved created by Accident that allways works no matter what number is put in (I finally got the second turtle working)
# # # # org = turtle.position()
# # # # while True:
# # # #   t1.forward(90)
# # # #   t1.right(60)
# # # #   p = t1.position()
# # # #   for i in range(100):
# # # #     t2.setpos(p)
# # # #     t2.forward(90)
# # # #     t2.right(60)
# # # #   p = t1.position()
# # # #   print(p)
# # # #   d = t1.distance((org)) 
# # # #   if d < 0.1:
# # # #     break

num = [1, 2, 3, 4, 5, 6]
state = []
state1 = []
state2 = []
state3 = []
state4 = []
state5 = []
state6 = []
rand_state_list = [state1, state2, state3, state4, state5, state6]
rand_state_list2 = [state1, state2, state3, state4, state5, state6]
rand_state_list3 = [state1, state2, state3, state4, state5, state6]
tlist = [t2, t3, t4, t5, t6, t7]
tlist6 = [t2, t3, t4, t5, t6, t7]

org = t1.position()
while True:
  t1.forward(50)
  t1.right(60)
  p = t1.position()
  h = t1.heading()
  state_pair = [p, h]
  state.append(state_pair)
  d = t1.distance((org))
  if d < 0.1:
    t1.end_fill()
    break


# random.shuffle(tlist)
# random.shuffle(state)
for i in range(len(tlist)):
  t = tlist[i]
  s = state[i]
  c = s[0]
  h = s[1]
  t.penup()
  # vertex of original shape
  t.goto(c)
  t.setheading(h)
  t.pendown()


for i in range(len(state)):
  tt = tlist[i]
  tt.begin_fill()

# while True:
#   random.shuffle(tlist)
#   ttt = tlist[i]
#   orgorg = ttt.position()
#   while True:
#     ttt.forward(50)
#     ttt.left(60)
#     # pp = ttt.position()
#     # state.append(pp)
#     dd = ttt.distance((orgorg))
#     if dd < 0.1:
#       ttt.end_fill()
#       break

# for i in range(len(tlist)):
#   ttt = tlist[i]
#   orgorg = ttt.position()
#   while True:
#     s = state[i]
#     c = s[0]
#     p = ttt.position()
#     h = ttt.heading()
#     state_pair2 = [p, h]
#     state.append(state_pair2)
#     ttt.forward(50)
#     ttt.left(60)
#     pp = ttt.position()
#     state.append(pp)
#     dd = ttt.distance((orgorg))
#     if dd < 0.1:
#       ttt.end_fill()
#       break

for j in range(3):
  state_new = []
  for i in range(len(tlist)):
    ttt = tlist[i]
    p, h = state[i]
    print(state[i])
    ttt.setpos(p)
    ttt.setheading(h)
    orgorg = ttt.position()
    for k in range(6):
      # s = state[i]
      # c = s[0]
      ttt.forward(50)
      ttt.left(60)
      if k == 3:
        p = ttt.position()
        h = ttt.heading()
        print(f"s={(p, h-120)}")
        state_new.append((p, h - 120))
      # pp = ttt.position()
      # state.append(pp)
      dd = ttt.distance((orgorg))
      if dd < 0.1:
        ttt.end_fill()
        break
  state = state_new
  print()
  time.sleep(2)
  

# while True:
#   if len(tlist3) == 0:
#         break
#   ttt = random.choice(tlist3)
#   orgorg = ttt.position()
#   while True:
#     ttt.forward(50)
#     ttt.left(60)
#     # pp = ttt.position()
#     # state.append(pp)
#     dd = ttt.distance((orgorg))
#     if dd < 0.1:
#       ttt.end_fill()
#       tlist3.remove(ttt)
#       break

# # First Layer
# while True:
#   if len(tlist3) == 0:
#         break
#   rand_list = random.choice(rand_state_list)
#   ttt = random.choice(tlist3)
#   orgorg = ttt.position()
#   while True:
#     ttt.forward(50)
#     ttt.left(60)
#     p2 = ttt.position()
#     h2 = ttt.heading()
#     state_pair = [p2, h2]
#     rand_list.append(state_pair)
#     dd = ttt.distance((orgorg))
#     if dd < 0.1:
#       ttt.end_fill()
#       rand_state_list.remove(rand_list)
#       tlist3.remove(ttt)
#       break

# # while True:
# #   if len(tlist3) == 0:
# #         break
# #   rand_list = random.choice(rand_state_list)
# #   ttt = random.choice(tlist3)
# #   orgorg = ttt.position()
# #   while True:
# #     ttt.forward(50)
# #     ttt.left(60)
# #     p2 = ttt.position()
# #     h2 = ttt.heading()
# #     state_pair = [p2, h2]
# #     rand_list.append(state_pair)
# #     dd = ttt.distance((orgorg))
# #     if dd < 0.1:
# #       ttt.end_fill()
# #       rand_state_list.remove(rand_list)
# #       tlist3.remove(ttt)
# #       break

# for i in range(len(state1)):
#   print(state1[i])

# while True:
#   rand_list = random.choice(rand_state_list2)
#   rand_list.pop(0)
#   rand_list.pop(1)
#   rand_list.pop(13)
#   rand_state_list2.remove(rand_list)
#   if len(rand_state_list2) == 4:
#     break

# # here







# random.shuffle(state)
# random.shuffle(tlist)
# for i in range(len(tlist)):
#   tr = tlist[i]
#   s = state[i]
#   while True:
#     c2 = s[0]
#     h2 = s[1]
#     tr.penup()
#     tr.goto(c)
#     tr.setheading(h)
#     tr.pendown()
#     break




  

# while True:
#   if len(tlist4) == 0:
#         break
#   while True:
#     tr = random.choice(tlist4)
#     s = random.choice(state1)
#     c = s[0]
#     h = s[1]
#     tr.penup()
#     tr.goto(c)
#     tr.setheading(h)
#     tr.pendown()
#     tlist4.remove(tr) 
#     state1.remove(s)
#     if len(state1) == 0:
#       break

# while True:
#   tt = random.choice(tlist5)
#   tt.begin_fill()
#   tlist5.remove(tt)
#   if len(tlist5) == 0:
#     break

# while True:
#   if len(tlist6) == 0:
#         break
#   ttt = random.choice(tlist6)
#   orgorg = ttt.position()
#   while True:
#     ttt.forward(50)
#     ttt.left(60)
#     dd = ttt.distance((orgorg))
#     if dd < 0.1:
#       ttt.end_fill()
#       tlist6.remove(ttt)
#       break