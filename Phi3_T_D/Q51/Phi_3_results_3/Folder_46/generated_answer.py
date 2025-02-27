from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_buckets = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_buckets[sorted_str].append(string)
    anagram_pairs = sum([len(p) * (len(p) - 1) // 2 for p in anagram_buckets.values()])
    return anagram_pairs <= 61