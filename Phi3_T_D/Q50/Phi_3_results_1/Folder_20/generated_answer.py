from collections import defaultdict
from itertools import permutations

def if_contains_anagrams(words):
    anagrams_set = defaultdict(set)
    for word in words:
        if len(word) < 3 or not word.isalpha():
            continue
        sorted_word = ''.join(sorted(word.lower())).replace(' ', '')
        for perm in permutations(sorted_word):
            anagram = ''.join(perm)
            anagrams_set[anagram].add(word.lower())
    return sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagrams_set.values())) >= 64