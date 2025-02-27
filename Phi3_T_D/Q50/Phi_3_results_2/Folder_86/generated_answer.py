from collections import defaultdict

def if_contains_anagrams(string_list):
    sorted_anagrams = defaultdict(list)
    for s in string_list:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            sorted_anagrams[sorted_str].append(s)
    anagram_pairs = 0
    for anagrams in sorted_anagrams.values():
        if len(anagrams) > 1:
            pair_count = len(anagrams) * (len(anagrams) - 1) // 2
            anagram_pairs += pair_count
    return anagram_pairs >= 115