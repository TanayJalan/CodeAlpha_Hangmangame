import random

print(["python", "coding", "college", "program", "computer",
       "developer", "keyboard", "internet", "software", "hardware",
       "database", "algorithm", "function", "variable", "compiler",
       "network", "terminal", "laptop", "debugging", "framework"])

print("Guess the word from the above list")

words = [
    "python", "coding", "college", "program", "computer",
    "developer", "keyboard", "internet", "software", "hardware",
    "database", "algorithm", "function", "variable", "compiler",
    "network", "terminal", "laptop", "debugging", "framework"
]

secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman")

while wrong_guesses < max_wrong:
    display = ""

    for ch in secret_word:
        if ch in guessed_letters:
            display += ch + " "
        else:
            display += "_ "

    print("\nWord:", display.strip())
    print("Attempts left:", max_wrong - wrong_guesses)

    if "_" not in display:
        print("You won the game!")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha() or guess in guessed_letters:
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        wrong_guesses += 1

if wrong_guesses == max_wrong:
    print("\nGame over")