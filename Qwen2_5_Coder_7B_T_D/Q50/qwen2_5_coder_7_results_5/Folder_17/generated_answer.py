from collections import defaultdict

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s))
        anagram_dict[sorted_s].append(s)
    anagram_pairs = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            anagram_pairs += len(anagram_dict[key]) - 1
    return anagram_pairs >= 97