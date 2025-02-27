from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = Counter()
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            anagram_counts[normalize(s)] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 29