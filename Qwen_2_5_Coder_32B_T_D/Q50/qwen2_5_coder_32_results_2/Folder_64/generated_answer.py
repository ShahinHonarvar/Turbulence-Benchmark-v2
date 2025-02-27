from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        key = tuple(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[key].append(word)
    return sum((len(v) > 1 for v in anagrams.values())) >= 5