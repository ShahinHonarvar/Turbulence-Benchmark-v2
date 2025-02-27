from collections import defaultdict

def if_contains_anagrams(words):
    word_count = defaultdict(int)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            word_count[sorted_word] += 1
    anagram_pairs = sum((c * (c - 1) // 2 for c in word_count.values()))
    return anagram_pairs >= 108