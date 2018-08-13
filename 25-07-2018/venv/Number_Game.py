import random

while(5>1):
    think = random.randint(1, 10)
    num = int(input("I'm thinking of a number in range 1 to 10, Can you guess it??...\n"))

    question = input("Enter your Question: ")


    if(num == think):
        print("Lucky Guess....")
    else:
        print("I know you are a dumb...")