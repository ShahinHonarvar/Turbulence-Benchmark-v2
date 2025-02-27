from itertools import permutations

def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def palindromes_between_indices(s):
    substring = s[5:10]
    letters = ''.join(filter(str.isalpha, substring)).lower()
    palindromes = set()
    if len(letters) >= 6:
        for p in permutations(letters, 6):
            candidate = ''.join(p)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes