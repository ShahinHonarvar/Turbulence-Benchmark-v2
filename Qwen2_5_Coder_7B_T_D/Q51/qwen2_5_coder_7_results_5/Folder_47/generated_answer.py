from collections import Counter

def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if s in anagram_dict:
                anagram_dict[s].append(s)
            else:
                anagram_dict[s] = [s]
    anagram_pairs = 0
    for key, value in anagram_dict.items():
        if len(value) > 1:
            anagram_pairs += len(value) * (len(value) - 1) // 2
    return anagram_pairs <= 366