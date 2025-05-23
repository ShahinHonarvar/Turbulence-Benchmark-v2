from collections import defaultdict

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if s.isalpha() and len(s) >= 3]
    anagram_dict = defaultdict(int)
    for s in strings:
        sorted_s = ''.join(sorted(s))
        anagram_dict[sorted_s] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs <= 41