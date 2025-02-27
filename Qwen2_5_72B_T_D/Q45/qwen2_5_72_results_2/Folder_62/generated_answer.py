from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    substring = s[0:9]
    counter = Counter(substring.lower())
    middle_chars = [char for char, count in counter.items() if count % 2 == 1]
    if len(middle_chars) > 1:
        return set()
    half_palindrome_chars = [char * (count // 2) for char, count in counter.items()]
    half_palindrome = ''.join(half_palindrome_chars)
    palindromes = set()
    for i in range(len(half_palindrome) + 1):
        for j in range(i + 1, len(half_palindrome) + 1):
            half_permutations = [''.join(p) for p in set(permutations(half_palindrome[i:j]))]
            for half in half_permutations:
                if len(half) * 2 + len(middle_chars) >= 7:
                    palindrome = half + ''.join(middle_chars) + half[::-1]
                    palindromes.add(palindrome)
    return palindromes