from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = tuple(sorted(word_lower))
            anagrams[sorted_word].append(word_lower)
    pairs = 0
    for group in anagrams.values():
        n = len(group)
        pairs += n * (n - 1) // 2
        if pairs >= 72:
            return True
    return False