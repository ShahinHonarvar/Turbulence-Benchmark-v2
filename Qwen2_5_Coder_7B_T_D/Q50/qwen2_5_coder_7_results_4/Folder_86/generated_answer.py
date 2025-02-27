from collections import defaultdict

def if_contains_anagrams(strings):

    def count_anagrams(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_dict[count_anagrams(s)].append(s)
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values() if len(v) > 1))
    return pairs >= 115