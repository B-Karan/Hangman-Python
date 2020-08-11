import time
import random
from os import system
from words import word_list

hangman_status =[
'''
    -----------
    |         |
    |         O
    |        /|\\
    |         |
    |        / \\
    |
  -----
''',
'''
    -----------
    |         |
    |         O
    |        /|\\
    |         |
    |
    |
  -----
''',
'''
    -----------
    |         |
    |         O
    |         |
    |         |
    |
    |
  -----
''',
'''
    -----------
    |         |
    |         O
    |         |
    |
    |
    |
  -----
''',
'''
    -----------
    |         |
    |         O
    |
    |
    |
    |
  -----
''',
'''
    -----------
    |         |
    |
    |
    |
    |
    |
  -----
''',
'''
    -----------
    |
    |
    |
    |
    |
    |
  -----
'''
]

def play(word):
    ''' Takes the word and plays the game '''
    tries = 6
    guessed_letters = []
    answer = ["_" for i in range(len(word))]
    guessed = False
    message = ""
    print(hangman_status[tries])
    print(" ".join(answer))
    print("\n")
    while not guessed and tries > 0:
        user_guess = input("Enter Letter: ")
        if user_guess in word:
            if user_guess in guessed_letters:
                message = f"You Already Guessed {user_guess.upper()} letter."
            else:
                guessed_letters.append(user_guess)
                message = f"You Guessed Right! {user_guess.upper()} is in word."
                for i in range(len(word)):
                    if word[i] == user_guess:
                        answer[i] = word[i].upper()
        else:
            tries -= 1
            message = f"Oops! Your Guess was Incorrect! {tries} tries Left. Try Again."
        system("cls")
        print(hangman_status[tries])
        print(" ".join(answer))
        print("\n")
        print(message)


        if "".join(answer) == word or "_" not in answer:
            guessed = True
    if guessed:
        print("Congratulations!! You guessed the word..")
    else:
        print("Sorry!! You ran out of tries.")
        print(f"The word was {word.upper()}.")
    return

if __name__ == '__main__':
    while True:
        system("cls")
        word = random.choice(word_list)
        play(word)
        choice = input("Do you want to play again?[Y/N]: ")
        if not choice.lower() == "y":
            break
