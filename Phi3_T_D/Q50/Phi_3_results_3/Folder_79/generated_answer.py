def if_contains_anagrams(strings):
    sorted_strings = {''.join(sorted(s.lower())): [] for s in strings if len(s) >= 3}
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            sorted_strings[sorted_s].append(s)
    anagram_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in sorted_strings.values()))
    return anagram_pairs >= 40