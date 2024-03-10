#welcome statement
from art import logo, vs
from game_data import data
print(logo)
#array of choices 
import random
#while loop
win = True
score = 0
#while win:
#compare 2
while win:
  optionA = random.choice(list(data))
  optionB = random.choice(list(data)) 
  while optionA == optionB:
    optionB = random.choice(list(data))
  print(optionA["name"] + " - " + optionA["description"] +     ", " + optionA["country"])
  print(vs)
  print(optionB["name"] + " - " + optionA["description"] +     ", " + optionA["country"])
  choice = input("Enter higher or lower?")
#check answer
  if optionA["follower_count"] > optionB["follower_count"]:
    if choice == "higher":
      win = True
    else:
      win = False

  elif optionA["follower_count"] < optionB["follower_count"]:
    if choice == "lower":
      win = True
    else:
      win = False

  if win is True:
    score += 1
  else:
    print("You lose")
    break
#   if answer == True:
# #compare again & score +1
#     score += 1
#     win = True 
# #choice == False 
#   else:
# #break & show score
