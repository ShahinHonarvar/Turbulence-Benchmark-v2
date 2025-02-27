from collections import defaultdict

def if_contains_anagrams(strings):

    def anagram_key(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagrams[anagram_key(s)].append(s)
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1))
    return pairs <= 69