import nltk
from nltk.corpus import words
import random

# Download the NLTK word corpus if we haven't already
nltk.download('words')

# Get all English words
english_words = words.words()

# Keep only 5-letter words
five_letter_words = [word.lower() for word in english_words if len(word) == 5]

#print(f"There are {len(five_letter_words)} 5-letter words in the English language.")
#print(five_letter_words[:10])  # Print the first 10 5-letter words

def get_feedback(guess, solution):
    feedback = [''] * 5
    for i in range(5):
        if guess[i] == solution[i]:
            feedback[i] = 'G'
        elif guess[i] in solution:
            feedback[i] = 'Y'
        else:
            feedback[i] = '-'
    return feedback

#def filter_words(word_list, guess, feedback):
    green_positions = {i: guess[i] for i in range(5) if feedback[i] == 'G'}
    yellow_positions = {i: guess[i] for i in range(5) if feedback[i] == 'Y'}
    
    filtered_words = []
    for word in word_list:
        match = True
        
        # Check green positions
        for pos, char in green_positions.items():
            if word[pos] != char:
                match = False
                break
        
        # Check yellow positions
        if match:
            for pos, char in yellow_positions.items():
                if word[pos] == char or char not in word:
                    match = False
                    break
        
        # Check gray positions
        if match:
            for i in range(5):
                if feedback[i] == '-' and guess[i] in word:
                    match = False
                    break
        
        if match:
            filtered_words.append(word)
    
    return filtered_words

def filter_words(word_list, guess, feedback):
    green_positions = {i: guess[i] for i in range(5) if feedback[i] == 'G'}
    yellow_positions = {i: guess[i] for i in range(5) if feedback[i] == 'Y'}
    
    filtered_words = []
    for word in word_list:
        if all(word[pos] == char for pos, char in green_positions.items()) and \
           all(word[pos] != char and char in word for pos, char in yellow_positions.items()):
            filtered_words.append(word)
    
    return filtered_words


def wordle_solver(word_list):
    possible_words = word_list[:]
    attempts = 0
    
    while attempts < 6:
        guess = random.choice(possible_words)  # For simplicity, start with a random guess
        
        # Simulate feedback for demonstration purposes (replace with actual feedback in practice)
        # In a real scenario, you would receive feedback after each guess from the game
        solution = "swish"  # Example solution
        feedback = get_feedback(guess, solution)
        
        feedback_str = ''.join(feedback)  # Convert feedback list to a string for display
        print(f"Attempt {attempts + 1}: {guess} - Feedback: {feedback_str}")
        
        if feedback == ['G'] * 5:
            print(f"Solved in {attempts + 1} attempts! Solution: {guess}")
            return guess
        
        possible_words = filter_words(possible_words, guess, feedback)
        attempts += 1
        
    print("Failed to solve the Wordle.")
    return None

# Example usage
wordle_solver(five_letter_words)