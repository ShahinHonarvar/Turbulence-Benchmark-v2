from collections import defaultdict

def if_contains_anagrams(words):
    anagram_buckets = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_buckets[sorted_word].append(word)
    pairs_of_anagrams = 0
    for bucket in anagram_buckets.values():
        if len(bucket) >= 2:
            pairs_of_anagrams += len(bucket) * (len(bucket) - 1) // 2
    return pairs_of_anagrams <= 77