from collections import Counter

def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
    for group in anagram_dict.values():
        if len(group) > 1:
            count = len(group) - 1
            if count * (count + 1) // 2 > 81:
                return False
    return True