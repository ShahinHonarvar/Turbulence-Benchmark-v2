from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_buckets = defaultdict(list)
    for string in strings:
        length = len(string)
        if length < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        anagram_buckets[sorted_str].append(string)
    count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_buckets.values()))
    return count <= 401