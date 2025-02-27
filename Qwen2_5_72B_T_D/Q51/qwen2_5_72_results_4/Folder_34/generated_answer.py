from collections import defaultdict

def if_contains_anagrams(words):
    anagram_counts = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_counts[sorted_word] += 1
    pairs_of_anagrams = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs_of_anagrams <= 401