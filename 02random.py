import random  # random mdoule
n=random.randint(1,100)   #we can change number from here 
a=-1
guesses=0   
while(a !=n):
    guesses+=1
    a=int(input("guess a number "))
    if(a>n):
        print("too high")

    else:
        print("higher number pls")    

print(f"(you guessed the number {guesses} guesses)")
