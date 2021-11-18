#!/usr/bin/env python
# coding: utf-8

# In[2]:


def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the Movie")
guess1 = input("Which movie made keenu reeves famous? ")
check_guess(guess1, "matrix")
guess2 = input("Which movie own oscar and directed by danny bowle? ")
check_guess(guess2, "slumdog millionaire")
guess3 = input("Which movie kate winslet and leonardo d caprios starred that won many oscars? ")
check_guess(guess3, "titanic")
print("Your Score is "+ str(score))


# In[ ]:




