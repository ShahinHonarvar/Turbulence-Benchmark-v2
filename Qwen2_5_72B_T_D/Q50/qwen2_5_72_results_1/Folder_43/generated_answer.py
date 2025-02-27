from collections import Counter

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count = Counter()
    for word in lst:
        if len(word) >= 3:
            count[normalize(word)] += 1
    anagram_pairs = sum((c * (c - 1) // 2 for c in count.values()))
    return anagram_pairs >= 61