from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = set(s)
    palindromes = set()
    for word_length in range(5, len(s) + 1):
        for perm in set(permutations(letters, word_length)):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes