def if_contains_anagrams(lst: list) -> bool:
    count = 0
    anagram_dict = {}
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s not in anagram_dict:
            anagram_dict[sorted_s] = [s]
        else:
            anagram_dict[sorted_s].append(s)
    for sorted_s, anagrams in anagram_dict.items():
        if len(anagrams) >= 2 and len(sorted_s) >= 3:
            count += 1
    return count >= 89