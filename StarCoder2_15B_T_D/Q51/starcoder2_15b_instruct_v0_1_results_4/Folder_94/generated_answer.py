import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_sorted = ''.join(sorted(s.lower()))
        if len(s_sorted) >= 3:
            if s_sorted in anagrams:
                anagrams[s_sorted].append(s)
            else:
                anagrams[s_sorted] = [s]
    num_anagrams = 0
    for anagram_group in anagrams.values():
        num_anagrams += len(list(itertools.combinations(anagram_group, 2)))
    return num_anagrams <= 181