from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(input_string):
    substring = input_string[2:9]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    letters_set = set(letters)
    palindromes = set()
    length = len(letters)
    if length < 6:
        return palindromes
    for perm in permutations(sorted(letters_set), length):
        candidate = ''.join(perm)
        if is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes