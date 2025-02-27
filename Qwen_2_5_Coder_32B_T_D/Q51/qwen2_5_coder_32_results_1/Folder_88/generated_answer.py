from collections import defaultdict

def if_contains_anagrams(words):
    anagram_counts = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_counts[sorted_word] += 1
    pairs_of_anagrams = sum((v * (v - 1) // 2 for v in anagram_counts.values()))
    return pairs_of_anagrams <= 407