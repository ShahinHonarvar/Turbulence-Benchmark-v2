from collections import defaultdict

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_dict = defaultdict(int)
    for s in strings:
        sorted_s = ''.join(sorted(s))
        anagram_dict[sorted_s] += 1
    anagram_pairs = sum((count - 1 for count in anagram_dict.values() if count > 1))
    return anagram_pairs >= 26