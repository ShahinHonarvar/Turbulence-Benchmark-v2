from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[key].append(word)
    count = sum((1 for v in anagrams.values() if len(v) > 1))
    return count <= 3