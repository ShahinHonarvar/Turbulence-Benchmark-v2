from collections import defaultdict

def if_contains_anagrams(words):
    anagram_counts = defaultdict(int)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            anagram_counts[sorted_word] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pair_count <= 16