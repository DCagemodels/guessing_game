import random

# Global variable for chances
chances = 10

# Introduction
introString = "Welcome to the guessing game, Let's have some fun!"
print(introString)

# Random word Selected from List
def Word_Selection():
    wordList = ['apple', 'banana', 'orange', 'grape', 'watermelon', 'pineapple', 'strawberry', 
    'blueberry', 'peach', 'plum', 'pear', 'kiwi', 'mango', 'apricot', 'lemon', 
    'lime', 'cherry', 'raspberry', 'blackberry', 'pomegranate']
    
    wordChoice = random.choice(wordList)
    wordCount = wordChoice
    print(f"There are {len(wordCount)} letters")
    return wordChoice

# Players guess a letter then wordCount reduced
def Player_One_Guess(chosenWord, chances):
    guessedLetters = []
    while chances > 0:
        guessType = input("What do you want to guess? Type 'letter' for a single letter or 'word' for the entire word: ").lower()
        if guessType == 'letter':
            guessedLetter = input("What letter do you choose: ")
            if guessedLetter in guessedLetters:
                print("You already guessed that letter.")
            else:
                guessedLetters.append(guessedLetter)
                if guessedLetter in chosenWord:
                    print(f"Yes, '{guessedLetter}' is in the word!")
                else:
                    print(f"Sorry, '{guessedLetter}' is not in the word.")
                    chances -= 1
        elif guessType == 'word':
            guessedWord = input("Can you guess the word? ")
            if guessedWord.lower() == chosenWord:
                print(f"Congratulations! You guessed the word: '{chosenWord}'")
                break
            else:
                print("Wrong guess!")
                chances -= 1
        else:
            print("Please enter 'letter' or 'word'.")
            continue
        
        print(f"You have {chances} chances left.")
        if set(chosenWord).issubset(set(guessedLetters)):
            print(f"Congratulations! You guessed the word: '{chosenWord}'")
            break
    else:
        print(f"Sorry, you ran out of chances. The word was '{chosenWord}'.")

# Main game logic
def Main_Game():
    chosenWord = Word_Selection()
    Player_One_Guess(chosenWord, chances)

# Start the game if executed as a script
if __name__ == "__main__":
    Main_Game()