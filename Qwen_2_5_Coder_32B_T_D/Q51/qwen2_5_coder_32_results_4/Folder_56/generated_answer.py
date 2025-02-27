from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        key = tuple(sorted(word.lower()))
        if len(word) >= 3:
            anagram_count[key] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 11