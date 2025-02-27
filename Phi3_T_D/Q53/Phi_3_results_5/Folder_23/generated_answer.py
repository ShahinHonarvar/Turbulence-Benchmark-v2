import re
from itertools import combinations

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    letters = re.findall('[a-z]', s)
    for i in range(19, len(s) + 1):
        for combo in combinations(letters, i):
            candidate = ''.join(combo)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes