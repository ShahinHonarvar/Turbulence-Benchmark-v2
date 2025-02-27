from itertools import permutations
from collections import Counter

def palindromes_between_indices(s):
    substring = s[5:10].lower()
    letters = [char for char in substring if char.isalpha()]
    counter = Counter(letters)
    palindrome_set = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindrome_set.add(''.join(perm))
    return palindrome_set