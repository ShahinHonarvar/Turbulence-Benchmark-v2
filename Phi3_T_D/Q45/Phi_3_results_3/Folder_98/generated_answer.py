from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(input_string):
    relevant_chars = input_string[3:6].lower()
    letters = ''.join(filter(str.isalpha, relevant_chars))
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            candidate = ''.join(perm)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes