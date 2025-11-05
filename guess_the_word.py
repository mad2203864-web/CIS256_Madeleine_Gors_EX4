import random

# list of random words
word_list = ['fine', 'good', 'mood',
             'extra', 'two', 'see', 'key',
             'why', 'great', 'need', 'mother',
             'father', 'sister', 'brother',
             'kid', 'child', 'children',
             'lemon', 'apple', 'leap',
             'bread', 'sad', 'money']

def main ():

  # selects a word from list
  word = random.choice(list)

  # sets number of attempts and defines the word as a set
  guessed_letters = set()
  attempts = 10

  print("\nWord Guess")

  # keeps looping as long as attempts are above 0
  while attempts > 0:
    # user inputs guessed letter
    guess = input("\nEnter one letter: ").lower()

    # decreases the number of guesses
    attempts -= 1

    # checks if letter has already been guessed
    if guess in guessed_letters:
      print("\nAlready guessed. Try another letter.")
      continue
    # adds letter to guessed word if correct or lets user know if letter is incorrect
    if guess in word:
      guessed_letters.add(guess)
      print("\nLetter is correct.")
    else:
      print("\nLetter is incorrect. Try again.")

    # displays the word and current number of attempts
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print("\nCurrent word:", display_word)
    print("\nCurrent attempts:", attempts)

    # displays if word is correctly guessed
    if "_" not in display_word.replace(" ", ""):
      print("\nWord is correct!")
      print("\nWord is:", word)
      return
    
  # prints if attempts reach 0 & word isn't guessed
  print("\nOut of attempts. Word is:", word)

if __name__ == "__main__":
    main()

