from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        w = word.lower()
        if len(w) >= 3:
            sorted_word = ''.join(sorted(w))
            anagram_count[sorted_word] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values() if v >= 2))
    return pairs >= 36