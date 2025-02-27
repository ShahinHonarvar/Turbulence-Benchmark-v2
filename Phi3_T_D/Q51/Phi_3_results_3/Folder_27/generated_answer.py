from collections import defaultdict

def if_contains_anagrams(lst):

    def sort_chars(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagrams[sort_chars(word)] += 1
    pairs = sum((x * (x - 1) // 2 for x in anagrams.values()))
    return pairs <= 113