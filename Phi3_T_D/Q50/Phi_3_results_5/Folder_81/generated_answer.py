from collections import defaultdict

def if_contains_anagrams(strings):

    def get_normalized(s):
        return ''.join(sorted(s.lower()))
    anagram_buckets = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            normalized = get_normalized(s)
            anagram_buckets[normalized].append(s)
    pairs_count = 0
    for bucket in anagram_buckets.values():
        pairs_count += len(bucket) * (len(bucket) - 1) // 2
    return pairs_count >= 16