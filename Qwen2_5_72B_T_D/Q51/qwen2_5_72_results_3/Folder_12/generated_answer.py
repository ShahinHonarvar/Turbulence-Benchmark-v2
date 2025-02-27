from collections import defaultdict

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3 and s.isalpha()]
    anagram_dict = defaultdict(int)
    for s in strings:
        sorted_s = ''.join(sorted(s))
        anagram_dict[sorted_s] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs <= 92