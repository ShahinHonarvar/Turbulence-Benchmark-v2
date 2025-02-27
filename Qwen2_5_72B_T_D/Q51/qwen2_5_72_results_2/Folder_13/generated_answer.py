from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            count[normalize(word)] += 1
    anagram_pairs = sum((c * (c - 1) // 2 for c in count.values()))
    return anagram_pairs <= 54