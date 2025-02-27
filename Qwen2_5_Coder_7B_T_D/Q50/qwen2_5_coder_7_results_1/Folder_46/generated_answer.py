from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    d = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            d[frozenset(word.lower())].append(word)
    anagram_pairs = 0
    for key in d:
        if len(d[key]) > 1:
            n = len(d[key])
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs >= 38