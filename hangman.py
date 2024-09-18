from hangman_words import words
import random
import string
def is_valid_number(words): # 2. list
    word = random.choice(words) # tour
    while ('-' in word) or (' ' in word): # if
        word = random.choice(words) # observe
        return word # observe
    return word.upper() # word = observe
def hangman():
    word = is_valid_number(words) # 1.
    #print(word)
    word_letters = set(word) # 3. letters in the word (word_letters = (o b s e r v e))
    alphabets = set(string.ascii_uppercase) # ABCDE....
    used_letters = set() # what a user has guessed -- A
    lives = 6

    # getting user input
    while (len(word_letters) > 0) and (lives > 0): # 4.true
        # letter that used
        print("You have", lives," lives left and You have used these letters: ", " ".join(used_letters))
        # 6 lives and - - usedletters

        # what current word is (----)
        word_list = [letter if letter in used_letters else "-" for letter in word]
        # if o in word,print(letter), else "-"
        print("current word: ", ' '.join(word_list)) # ----

        user_letter = input("Guess a letter: ").upper() # A
        if user_letter in (alphabets-used_letters):
            used_letters.add(user_letter) # add in used letters
            if user_letter in word_letters:
                word_letters.remove(user_letter) # remove
            else:
                lives -= 1 # decrease in lives
                print("Letter isn't in the word.")

        elif user_letter in used_letters:
            print("You have already used this letter.Try again..")
        else:
            print ("invalid!!")
    if lives == 0:
        return "Sry you have died!, the word is", word
    else:
        return f"You guessed the {word}"

print(hangman())
