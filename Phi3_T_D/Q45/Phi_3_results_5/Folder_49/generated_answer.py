from itertools import permutations

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_between_indices(text):
    required_letters = text[5:8]
    unique_letters = set(required_letters.lower())
    possible_palindromes = set()
    for perm in permutations(unique_letters, 3):
        palindrome = ''.join(perm) + ''.join(perm)[::-1]
        if is_palindrome(palindrome):
            possible_palindromes.add(palindrome)
    return possible_palindromes