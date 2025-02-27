from itertools import permutations

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_between_indices(text):
    start_index = min(4, len(text))
    end_index = min(5, len(text))
    substring = text[start_index:end_index + 1]
    letters = set(substring.lower())
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    possible_letters = letters.intersection(english_letters)
    if len(possible_letters) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(possible_letters) + 1):
        for combo in permutations(possible_letters, length):
            word = ''.join(combo)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes