from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_count[sorted_word] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pairs >= 140