from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_buckets = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_buckets[sorted_word].append(word)
    anagram_pairs = 0
    for anagram_group in anagram_buckets.values():
        size = len(anagram_group)
        if size >= 2:
            anagram_pairs += size * (size - 1) // 2
            if anagram_pairs > 188:
                return False
    return True