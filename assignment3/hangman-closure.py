# Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)
        displayed = "".join(c if c in guesses else "_" for c in secret_word)
        print(displayed)
        return all(c in guesses for c in secret_word)

    return hangman_closure


if __name__ == "__main__":
    secret_word = input("Enter the secret word: ")
    hangman = make_hangman(secret_word)
    while True:
        guess = input("Guess a letter: ")
        if not guess.strip():
            continue
        letter = guess.strip()[0]
        if hangman(letter):
            break
