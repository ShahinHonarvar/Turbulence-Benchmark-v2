from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = Counter()
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            count[normalize(s)] += 1
    anagram_pairs = sum((c * (c - 1) // 2 for c in count.values()))
    return anagram_pairs <= 188