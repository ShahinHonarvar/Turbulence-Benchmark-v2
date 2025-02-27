def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) < 3:
            continue
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s] += 1
        else:
            anagram_dict[sorted_s] = 1
    return any((count >= 2 for count in anagram_dict.values())) and len([v for v in anagram_dict.values() if v >= 2]) >= 5