import random

# Animal word list
words = [
    "tiger", "elephant", "giraffe", "kangaroo", "dolphin",
    "alligator", "butterfly", "penguin", "cheetah", "zebra",
    "rhinoceros", "hippopotamus", "chimpanzee", "crocodile", "flamingo"
]

# Choose a random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("🐾 Welcome to Animal Hangman!")

# Game loop
while wrong_guesses < max_attempts:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nAnimal:", display_word.strip())
    print("Wrong guesses left:", max_attempts - wrong_guesses)
    print("Guessed letters:", " ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()


    if not guess.isalpha() or len(guess) != 1:
        print("❌ Enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ Already guessed.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        print("❌ Wrong!")
        wrong_guesses += 1


    if all(letter in guessed_letters for letter in word):
        print("\n🎉 You guessed the animal:", word)
        break

if wrong_guesses == max_attempts:
    print("\n💀 Game Over! The animal was:", word)