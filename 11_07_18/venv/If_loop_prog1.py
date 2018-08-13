Roll = input("Enter your Roll number")
Class = input("Enter your Class")
Phy = int(input("How many Marks have you scored in Physics..?"))
FCP = int(input("How many Marks have you scored in FCP..?"))
Chem = int(input("How many Marks have you scored in Chemistry..?"))
M1 = int(input("How many Marks have you scored in LAC..?"))
M2 = int(input("How many Marks have you scored in DEAC..?"))


total = Phy+Chem+FCP+M1+M2
avg = total/5
percent = (total/500)*100

print(" ")
print(" ")
print(" ")
print("Roll Number: ", Roll, "          MIT-ADT University            Result Portal")
print("Your Percent is: ", percent)
print("")
print("Your Average Marks is: ", avg)
print("")
print("Physics Marks: ", Phy, "             DEAC Marks: ", M2, "            Chemistry Marks: ", Chem)
print("FCP Marks: ", FCP, "                                             LAC Marks: ", M1)
if(percent>=60 and percent>80):
    print("You've scored First class and distinction.")
elif(percent>60 and percent<80):
    print("You've scored first class.")
elif(percent<60 and percent>50):
    print("You've scored second class.")
elif(percent<50 and percent>40):
    print("You've scored third class.")
else:
    print("So sorry to say that you've failed.")
