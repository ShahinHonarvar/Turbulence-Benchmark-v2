from collections import Counter

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counts = Counter()
    for word in lst:
        if len(word) >= 3:
            counts[normalize(word)] += 1
    anagram_pairs = sum((1 for count in counts.values() if count >= 2))
    return anagram_pairs >= 21