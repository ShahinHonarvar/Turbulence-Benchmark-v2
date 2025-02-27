from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring_letters = set(substring.lower())
    palindrome_candidates = [char for char in substring if char in english_letters]
    if len(palindrome_candidates) < 5:
        return set()
    palindromes = set()
    for perm in permutations(palindrome_candidates, 5):
        if perm[0].isalpha():
            palindrome = ''.join(perm) + ''.join(reversed(perm))
            palindromes.add(palindrome.lower())
    return palindromes