from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return Counter(s.lower())
    anagrams = {}
    for s in strings:
        if len(s) >= 3:
            norm = frozenset(normalize(s).items())
            if norm in anagrams:
                anagrams[norm].add(s)
            else:
                anagrams[norm] = {s}
    anagram_pairs = sum((len(group) for group in anagrams.values() if len(group) > 1))
    return anagram_pairs <= 30