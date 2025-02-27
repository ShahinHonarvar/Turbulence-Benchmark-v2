import itertools
from collections import Counter

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def get_palindromes(letters, min_length):
    possible_palindromes = set()
    letters = Counter(letters[3:10].lower())
    remaining_letters = ''.join([letter * count for letter, count in letters.items()])
    for i in range(min_length, len(remaining_letters) + 1):
        for combination in itertools.combinations(remaining_letters, i):
            word = ''.join(combination)
            if is_palindrome(word):
                possible_palindromes.add(word)
    return possible_palindromes

def palindromes_between_indices(input_string):
    if len(input_string) < 10 or input_string[3] == ' ' or input_string[9] == ' ':
        return set()
    return get_palindromes(input_string, 7)