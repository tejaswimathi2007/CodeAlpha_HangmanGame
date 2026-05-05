import random
words=["apple","banana","grape","orange","peach"] #words list
word=random.choice(words)  
#game setup
guess_word=["_"]*len(word)
attempts=6
used_letters=[]
print("Welcome to Hangman!")
while attempts>0 and "_" in guess_word:        #game loop
    print("\nWord:","".join(guess_word))
    print("Attempts left:", attempts)
    print("Used letters:", " ".join(used_letters))
    guess=input("Enter a letter: ").lower()
    if len(guess)!=1 or not guess.isalpha():   #input validation
        print("Please enter a valid letter.")
        continue
    if guess in used_letters:                 #check repeated guess
        print("You already guessed that letter.")
        continue
    used_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guess_word[i]=guess
        print("Correct!")
    else:
        attempts-=1
        print("Wrong!")
        #result 
if "_" not in guess_word:
        print("\nCongratulations! You WON! You guessed the word:", word) 
else:
        print("\nGame Over! You LOST! The word was:", word)