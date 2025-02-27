from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_buckets = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            anagram_buckets[normalize(word)] += 1
    anagram_pairs = sum((freq * (freq - 1) // 2 for freq in anagram_buckets.values()))
    return anagram_pairs <= 81