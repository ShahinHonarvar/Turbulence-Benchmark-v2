from collections import defaultdict
from itertools import permutations

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))

    def has_anagram(word, word_hashes, min_len=3):
        if len(word) < min_len:
            return False
        normalized_word = normalize(word)
        if len(normalized_word) == min_len:
            return normalized_word in word_hashes
        return any((normalize(perm) in word_hashes for perm in permutations(word.lower()) if len(perm) == len(word)))
    anagram_hashes = defaultdict(int)
    for word in words:
        if has_anagram(word, anagram_hashes, 3):
            anagram_hashes[normalize(word)] += 1
    return sum((v >= 2 for v in anagram_hashes.values())) >= 188