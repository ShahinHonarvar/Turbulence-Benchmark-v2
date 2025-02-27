from itertools import permutations

def is_palindrome(word):
    return word == word[::-1]

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    letters = s[3:9].lower()
    possible_palindromes = set()
    for i in range(7, len(letters) + 1):
        for perm in permutations(letters, i):
            if is_palindrome(''.join(perm)):
                possible_palindromes.add(''.join(perm))
    return possible_palindromes