smallVowel = "a,e,i,o,u"
capitalVowel = "A,E,I.O,U"
space = " "
special = "`,~,!,@,#,$,%,^,&,*,(,),_,+,=,-"
consonents = "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z"
numbers = "0,1,2,3,4,5,6,7,8,9"
string = input("Enter the String to Check: ")

num_smallVowel=0
num_capitalVowel=0
num_space=0
num_special=0
num_Consonents=0
num_numbers=0
for j in string:
    if(j in smallVowel):
        num_smallVowel = num_smallVowel + 1
for k in string:
    if(k in special):
        num_special = num_special + 1
for m in string:
    if(m in space):
        num_space = num_space + 1
for n in string:
    if(n in capitalVowel):
        num_capitalVowel = num_capitalVowel + 1
for o in string:
    if(o in consonents):
        num_Consonents = num_Consonents + 1

for p in string:
    if(p in numbers):
        num_numbers = num_numbers + 1

print("Number of Small Vowels = ", num_smallVowel)
print("Number of Capital Vowels = ", num_capitalVowel)
print("Number of Spaces = ", num_space)
print("Number of Special = ", num_special)
print("Number of Consonents = ", num_Consonents)
print("Number of digits = ", num_numbers)