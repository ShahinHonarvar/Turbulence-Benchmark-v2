from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_count[sorted_word] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values() if v > 1))
    return pairs >= 123