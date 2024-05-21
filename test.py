import nltk
from nltk.corpus import words

import random

# Download the NLTK word corpus if we haven't already
nltk.download('words')

# Get all English words
english_words = words.words()

# Keep only 5 letter words
five_letter_words = [word.lower() for word in english_words if len(word) == 5]

#print(f"There are {len(five_letter_words)} 5-letter words in the English language.")
#print(five_letter_words[:10])  # Print the first 10 5-letter words

#picks a random word that matches the feedback from the previous guess
def get_next_move(guess, feedback, possible_words):
    #eliminate impossible options
    possible_words = [word for word in possible_words if matches_feedback(guess, word, feedback)]

    next_move = random.choice(possible_words)
    return next_move

def matches_feedback(guess, word, feedback):
    for i in range(len(guess)):
        if feedback[i] == '-':
            # If the feedback is '-', the letter in the guessed word
            # should not be present in the actual word.
            if word[i] in guess:
                return False
        elif feedback[i] == 'Y':
            # If the feedback is 'Y', the letter in the guessed word
            # should be present in the actual word but in the wrong position.
            if word[i] not in guess:
                return False
        elif feedback[i] == 'G':
            # If the feedback is 'G', the letter in the guessed word
            # should be present in the correct position in the actual word.
            if word[i] != guess[i]:
                return False
    # If all conditions are satisfied, the word matches the feedback.
    return True


# Main loop
MAX_GUESSES = 6
current_guess = "crate"  # First guess always "crate"
possible_words = five_letter_words.copy()

for _ in range(MAX_GUESSES):
    print("Guess:", current_guess)
    feedback = input("Feedback (e.g., 'G': correct letter and position, 'Y': correct letter but wrong position, '-': incorrect) example = --G-Y-: ")
    
    # Get next move
    current_guess = get_next_move(current_guess, feedback, possible_words)

    print("Next best move:", current_guess)