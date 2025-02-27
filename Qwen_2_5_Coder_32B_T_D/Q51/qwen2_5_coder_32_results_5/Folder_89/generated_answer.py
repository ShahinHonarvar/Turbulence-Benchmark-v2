from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            anagram_count[sorted_word] += 1
    pair_count = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pair_count <= 73