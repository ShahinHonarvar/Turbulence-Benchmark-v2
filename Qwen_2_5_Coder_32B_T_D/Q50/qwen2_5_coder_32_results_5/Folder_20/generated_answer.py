from itertools import combinations
    from collections import Counter

def if_contains_anagrams(words):
    words = [w.lower() for w in words if len(w) >= 3]
    sorted_words = [''.join(sorted(w)) for w in words]
    count = Counter(sorted_words)
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values() if v > 1))
    return anagram_pairs >= 64