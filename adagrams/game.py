from random import randint

def draw_letters():
    
    LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
    letter_pool = []
    for letter in LETTER_POOL:
        for _ in range(LETTER_POOL[letter]):
            letter_pool.append(letter)

    drawn_letters = []

    for _ in range(10):

        new_letter = letter_pool[randint(0, len(letter_pool) - 1)]
        letter_pool.remove(new_letter)
        drawn_letters.append(new_letter)

    return drawn_letters

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass
