from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagrams = Counter((''.join(sorted(word)) for word in words))
    count = sum((1 for v in anagrams.values() if v > 1))
    return count >= 73