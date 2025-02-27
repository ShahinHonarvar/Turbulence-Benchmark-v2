from collections import Counter

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = Counter()
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            anagrams[normalize(word)] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pairs <= 22