from itertools import combinations

def if_contains_anagrams(string_list):
    anagrams = {}
    for s in string_list:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    anagram_pairs = 0
    for k in anagrams:
        if len(anagrams[k]) > 1:
            anagram_pairs += len(list(combinations(anagrams[k], 2)))
    return anagram_pairs >= 41