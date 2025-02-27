from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            anagram_dict[''.join(sorted(s_lower))].append(s_lower)
    count = sum((1 for a in anagram_dict.values() if len(a) > 1 for i in range(len(a)) for j in range(i + 1, len(a))))
    return count >= 77