import random
word=["chin","talk","walk"]
random_int=random.choice(word)
print(random_int)
guess=input("guess the letter")
print(guess)
for letter in random_int:
 if(guess==letter): 
    print("right")
 else:
    print("wrong")