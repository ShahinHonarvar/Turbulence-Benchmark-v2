from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        normalized_word = ''.join(sorted(word.lower()))
        if len(normalized_word) >= 3:
            anagram_count[normalized_word] += 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pair_count <= 14