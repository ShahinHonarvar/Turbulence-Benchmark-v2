from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = Counter()
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            anagrams[normalize(s)] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pairs <= 77