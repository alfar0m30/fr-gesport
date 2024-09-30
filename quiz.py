import time
points = 0

print("Välkommen till frågesporten!\n ")
time.sleep(1.5)
answer = input("exempel fråga 1\n1) exemepel fråga 1\n2) exempel fråga 2\n3) exempel fråga 3\n\nSVAR: ")

if(answer == "3"):
    points += 1
    print("Rätt!\n")
    
else:
    print("Fel\n")

answer = input("exempel fråga 2\n1) exemepel fråga 1\n2) exempel fråga 2\n3) exempel fråga 3\n\nSVAR: ")
if(answer == "3"):
    points += 1
    print("Rätt!\n")
    
else:
    print("Fel\n")

print(f"Du fick {points} poäng")