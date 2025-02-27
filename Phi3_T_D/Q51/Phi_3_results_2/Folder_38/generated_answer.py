from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):
    alpha_words = [''.join(sorted((c for c in word.lower() if c.isalpha()))) for word in words]
    word_counts = defaultdict(int)
    for alpha_word in alpha_words:
        word_counts[alpha_word] += 1
    anagram_pairs = sum((1 for count in word_counts.values() if count > 1 and len(alpha_words) - count > 3))
    return anagram_pairs <= 416