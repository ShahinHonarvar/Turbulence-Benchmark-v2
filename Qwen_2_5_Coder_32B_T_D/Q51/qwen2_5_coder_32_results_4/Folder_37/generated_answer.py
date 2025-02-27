from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(words):
    count = 0
    anagram_map = defaultdict(list)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            anagram_map[w].append(word)
    for key in anagram_map:
        if len(anagram_map[key]) > 1:
            count += len(list(combinations(anagram_map[key], 2)))
        if count > 206:
            return False
    return True