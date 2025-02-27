from collections import Counter
from itertools import combinations

def palindromes_between_indices(s):
    substring = s[2:10]
    letter_counts = Counter(filter(str.isalpha, substring.lower()))
    available_letters = ''.join((k * (v // 2) for k, v in letter_counts.items()))
    even_centered = set()
    odd_centered = set()
    for i in range(2, 6):
        for letters in set(combinations(available_letters, i)):
            half_palindrome = ''.join(sorted(letters))
            even_centered.add(half_palindrome + half_palindrome[::-1])
            for center in letter_counts.keys():
                if letter_counts[center] % 2 == 1:
                    odd_centered.add(half_palindrome + center + half_palindrome[::-1])
    return even_centered.union(odd_centered)