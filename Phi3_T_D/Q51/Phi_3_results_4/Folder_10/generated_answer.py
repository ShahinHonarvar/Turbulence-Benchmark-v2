from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_sets = defaultdict(set)
    for word in lst:
        if len(word) >= 3:
            anagram_key = ''.join(sorted(word.lower()))
            anagram_sets[anagram_key].add(word.lower())
    anagram_pairs = 0
    for words in anagram_sets.values():
        anagram_pairs += len(words) * (len(words) - 1) // 2
    return anagram_pairs <= 21