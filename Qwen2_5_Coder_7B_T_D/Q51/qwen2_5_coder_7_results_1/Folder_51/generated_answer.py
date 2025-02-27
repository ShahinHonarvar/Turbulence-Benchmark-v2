from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s].append(s)
    pairs = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            pairs += len(anagram_dict[key]) - 1
    return pairs <= 116