from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            anagrams[tuple(sorted(word_lower))].append(word_lower)
    count = sum((1 for group in anagrams.values() if len(group) > 1))
    return count >= 5