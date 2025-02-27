from collections import defaultdict

def if_contains_anagrams(lst):

    def sort_signature(s):
        return ''.join(sorted(s.lower()))
    anagram_buckets = defaultdict(list)
    count = 0
    for item in lst:
        if len(item) >= 3:
            anagram_buckets[sort_signature(item)].append(item)
    for bucket in anagram_buckets.values():
        if len(bucket) >= 2:
            count += len(bucket) * (len(bucket) - 1) // 2
    return count >= 47