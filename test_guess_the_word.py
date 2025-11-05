import random
import pytest
from guess_the_word import word_list

def test_word_in_list():
    word = random.choice(word_list)
    assert word in word_list

def test_correct_guess():
    word = "kid"
    guessed_letters = set()
    guess = "k"
    guessed_letters.add(guess)
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    assert display_word[0] == "k"

def test_incorrect_guess():
    word = "kid"
    guessed_letters = set()
    guess = "x"
    guessed_letters.add(guess)
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    assert "x" not in display_word

