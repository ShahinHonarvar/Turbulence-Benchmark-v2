from collections import Counter

def if_contains_anagrams(strings):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    count = Counter()
    for s in strings:
        if len(s) >= 3:
            count[normalize_string(s)] += 1
    anagram_pairs = 0
    for c in count.values():
        anagram_pairs += c * (c - 1) // 2
    return anagram_pairs >= 61