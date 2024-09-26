import random

words = ["pizza","apple","plane","teeth","shirt"]
lives = 9
secret_word = random.choice(words)
clue = list("?????")
print(clue)
heart_symbol = u'\u2764'
print(heart_symbol)



while lives > 0:
    print(clue)
    print("lives left: " + heart_symbol * lives)
    guess = input("guess a letter or a whole word: ")


