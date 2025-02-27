from collections import Counter

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagram_dict = Counter([''.join(sorted(s)) for s in lst])
    count = sum((1 for count in anagram_dict.values() if count > 1))
    return count >= 144