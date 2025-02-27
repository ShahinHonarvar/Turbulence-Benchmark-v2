from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_pairs = 0
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        anagram_dict[sorted_s].append(s)
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        anagram_pairs += n * (n - 1) // 2
    return anagram_pairs >= 75