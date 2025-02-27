from collections import defaultdict, Counter

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[normalize(word)].append(word)
    return sum((len(group) >= 2 for group in anagrams.values())) >= 34