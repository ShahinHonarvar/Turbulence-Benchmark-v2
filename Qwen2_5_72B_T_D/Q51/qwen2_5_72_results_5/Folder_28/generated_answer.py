from collections import Counter

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = Counter()
    for word in lst:
        if len(word) >= 3:
            anagram_count[normalize(word)] += 1
    pairs = 0
    for count in anagram_count.values():
        pairs += count * (count - 1) // 2
    return pairs <= 78