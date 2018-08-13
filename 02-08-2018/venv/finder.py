# Write a menu driven program to find vowels, consonents, words, special characters, digits from given texts. Also convert upper case to lower case and vice versa

def check_vowels(string):
    vowels = "a,e,i,o,u,A,E,I,O,U"

    num_vowels=0
    for j in string:
        if(j in vowels):
            num_vowels = num_vowels + 1
    return num_vowels


def check_special(string):
    special = "`,~,!,@,#,$,%,^,&,*,(,),_,+,=,-"
    num_special=0
    for k in string:
        if(k in special):
            num_special = num_special + 1
    return num_special


def check_consonent(string):
    consonents = "b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z"
    num_Consonents=0
    for o in string:
        if(o in consonents):
            num_Consonents = num_Consonents + 1
    return num_Consonents


def check_numbers(string):
    numbers = "0,1,2,3,4,5,6,7,8,9"
    num_numbers=0
    for p in string:
        if(p in numbers):
            num_numbers = num_numbers + 1
    return num_numbers


def check_words(string):
    s = string
    s = string.split()
    num_words = len(s)
    return num_words

def changeCase(case):
    return ''.join(case.upper() if case in 'abcdefghijklmnopqrstuvwxyz' else case.lower() for case in string)

text = input("Enter the String: ")
choice = int(input("To perform: \n1: Vowels Count\n2: Special Characters Count\n3: Consonents Count\n4: Numbers Count\n5: Words Count\n6: Change the Case\nEnter your choice: "))
if (choice==1):
    count_vowels=check_vowels(text)
    print("Total Numbers of Vowels used: ", count_vowels)
elif (choice==2):
    count_special=check_special(text)
    print("Total Numbers of Vowels used: ", count_special)
elif (choice==3):
    count_consonents=check_consonent(text)
    print("Total Numbers of Consonents used: ", count_consonents)
elif (choice==4):
    count_numbers=check_numbers(text)
    print("Total Numbers of Numbers used: ", count_numbers)
elif (choice==5):
    count_words=check_words(text)
    print("Total Numbers of Words used: ", count_words)
elif (choice==6):
    change_case=changeCase(text)
    print("Total Numbers of Words used: ", change_case)
