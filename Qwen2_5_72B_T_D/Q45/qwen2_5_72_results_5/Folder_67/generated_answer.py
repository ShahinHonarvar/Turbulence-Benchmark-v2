from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:7].lower()
    counter = Counter(substring)
    even_parts = ''
    middle = ''
    for char, count in counter.items():
        even_parts += char * (count // 2)
        if count % 2 != 0 and (not middle):
            middle = char
    results = set()
    if len(even_parts) >= 2:
        for combination in set(permutations(even_parts, len(even_parts))):
            palindrome = ''.join(combination)
            if len(palindrome) * 2 + len(middle) >= 5:
                palindrome = palindrome + middle + palindrome[::-1]
                results.add(palindrome)
    return results