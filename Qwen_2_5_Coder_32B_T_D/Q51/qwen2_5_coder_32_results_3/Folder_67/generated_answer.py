from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        w = word.lower()
        if len(w) >= 3:
            anagrams[''.join(sorted(w))].append(w)
    return sum((len(v) > 1 for v in anagrams.values())) <= 5