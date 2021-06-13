from typing import Text



print("hello peeps to the quiz")

play=input("DO you want to play ? ")
if play != "yes":
    quit()
print("okay lets rumble")
score = 0 
ans=input("what does ccf stand for? ").lower()
if ans== "cosmic":
    print("based")
    score += 1
else:
    print("git good")
ans=input("what is nm? ")
if ans.lower()== "netmarble":
    print("based")
    score += 1
else:
    print("git good")
ans=input("who is thor bro? ")
if ans.upper()== "LOKI":
    print("based")
    score += 1
else:
    print("git good")
ans=input("how to get alot of crystals? ").upper()
if ans== "MONEY":
    print("based")
    score += 1
else:
    print("git good")    

print("you got " + str(score) + " questions correct ")
print("you scored " + str((score/4) * 100) + " %")