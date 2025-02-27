from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        w = word.lower()
        if len(w) >= 3:
            anagram_groups[''.join(sorted(w))].append(w)
    pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_groups.values()))
    return pairs <= 131