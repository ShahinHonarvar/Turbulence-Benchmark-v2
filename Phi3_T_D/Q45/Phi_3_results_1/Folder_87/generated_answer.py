from itertools import permutations

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_between_indices(s):
    subset_s = s[2:10]
    letters = set(subset_s.lower())
    palindromes = set()
    for i in range(3, min(len(subset_s) + 1, 11), 2):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if is_palindrome(word):
                palindromes.add(word.upper())
    return palindromes