from collections import defaultdict

def if_contains_anagrams(strings):

    def build_anagram_key(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = build_anagram_key(s)
            anagrams[key].append(s)
    anagram_pairs = 0
    for key, values in anagrams.items():
        anagram_pairs += len(values) * (len(values) - 1) // 2
    return anagram_pairs >= 52