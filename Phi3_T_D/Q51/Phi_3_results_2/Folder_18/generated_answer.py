from collections import defaultdict

def if_contains_anagrams(strings):

    def char_count(s):
        return ''.join(sorted(s.lower()))
    anagram_buckets = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = char_count(s)
            anagram_buckets[key].append(s)
    count = 0
    for bucket in anagram_buckets.values():
        pairs = len(bucket) * (len(bucket) - 1) // 2
        count += pairs
        if count > 42:
            return False
    return True