from itertools import permutations

def is_palindrome(word):
    return word == word[::-1]

def palindromes_between_indices(s):
    letters = set(s[3:10].lower())
    palindromes = set()
    for length in range(3, 10):
        for perm in set(permutations(letters, length)):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes