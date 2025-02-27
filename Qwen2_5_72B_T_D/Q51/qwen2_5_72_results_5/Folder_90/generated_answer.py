from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3 and s.isalpha()]
    anagram_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s)
        else:
            anagram_dict[sorted_s] = [s]
    anagram_counts = [len(lst) for lst in anagram_dict.values() if len(lst) > 1]
    anagram_pairs = sum([cnt * (cnt - 1) // 2 for cnt in anagram_counts])
    return anagram_pairs <= 147