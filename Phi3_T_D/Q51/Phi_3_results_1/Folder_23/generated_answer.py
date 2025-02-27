from collections import defaultdict
import math

def if_contains_anagrams(lst):
    length_count = len(lst)
    if length_count < 6:
        return True
    anagram_buckets = defaultdict(list)
    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        word_permutations = [''.join(p) for p in permutations(word)]
        anagram_buckets[word].extend(word_permutations)
    total_anagrams = 0
    seen = set()
    for perm_list in anagram_buckets.values():
        for word in perm_list:
            if word in seen:
                total_anagrams += 1
            seen.add(word)
    return total_anagrams <= 49