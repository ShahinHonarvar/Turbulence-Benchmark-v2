import re

def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        s = s.lower()
        if len(s) >= 3 and re.search('^[a-z]+$', s):
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s].append(s)
            else:
                anagram_dict[sorted_s] = [s]
    return len(anagram_dict) <= 91