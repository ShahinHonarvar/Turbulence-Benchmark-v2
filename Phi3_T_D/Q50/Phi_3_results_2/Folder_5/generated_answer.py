from collections import defaultdict

def if_contains_anagrams(words):

    def to_key(s):
        return ''.join(sorted(s.lower()))
    anagram_buckets = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            key = to_key(word)
            anagram_buckets[key].append(word)
    anagram_pairs_count = sum((len(bucket) * (len(bucket) - 1) // 2 for bucket in anagram_buckets.values()))
    return anagram_pairs_count >= 21