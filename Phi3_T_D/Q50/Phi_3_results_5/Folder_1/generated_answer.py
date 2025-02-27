from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):
    anagram_count = 0
    words = [word.lower() for word in words]

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_groups[''.join(sorted(word))].append(word)
    for group in anagram_groups.values():
        if len(group) > 1:
            combos = list(combinations(group, 2))
            anagram_count += len(combos)
    return anagram_count >= 96