import itertools
from collections import Counter

def normalize(s):
    return Counter(''.join(sorted(filter(str.isalpha, s.lower()))))

def is_anagram(a, b):
    return normalize(a) == normalize(b)

def calculate_anagram_pairs(words):
    pairs = list(itertools.combinations(words, 2))
    count = 0
    for word1, word2 in pairs:
        if is_anagram(word1, word2):
            count += 1
    return count

def if_contains_anagrams(strings):
    anagram_pairs = calculate_anagram_pairs(strings)
    return anagram_pairs <= 72