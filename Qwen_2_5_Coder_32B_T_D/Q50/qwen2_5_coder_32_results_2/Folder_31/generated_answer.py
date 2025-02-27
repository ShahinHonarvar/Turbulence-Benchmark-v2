from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    anagram_dict = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s] += 1
            else:
                anagram_dict[sorted_s] = 1
    for value in anagram_dict.values():
        if value > 1:
            count += value * (value - 1) // 2
    return count >= 68