points = 0
for i in range(10):
  from random import randint as rn
  x = [rn(0,10) for i in range(6)]
  y = [rn(0,10) for i in range(6)]
  listO = list(set(x))
  while len(listO) < 6:
    listO.append(rn(0,10))
    listO = list(set(listO))
  print(listO)
  listb = list(set(y))
  while len(listb) < 6:
    listb.append(rn(0,10))
    listb = list(set(listb))
  print(listb)
  user_input = int(input("please enter the a common number: "))
  if user_input in listb and user_input in listO:
    print("good job that was right")
    points += 1
    print("you have earned " + str(points) + " points so far")
  else:
    print("that was wrong")
    print("you have earned " + str(points) + " points so far" )
print("the game is finished.your score is: ")
print(points)
