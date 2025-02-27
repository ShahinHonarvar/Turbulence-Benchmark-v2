from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3 and s.isalpha()]
    anagram_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s))
        anagram_dict.setdefault(sorted_s, []).append(s)
    anagram_pairs_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs_count <= 65