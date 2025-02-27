def if_contains_anagrams(input_list):
    anagrams = {}
    for s in input_list:
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    anagram_pairs = [(k, v) for k, v in anagrams.items() if len(v) > 1]
    return len(anagram_pairs) >= 143