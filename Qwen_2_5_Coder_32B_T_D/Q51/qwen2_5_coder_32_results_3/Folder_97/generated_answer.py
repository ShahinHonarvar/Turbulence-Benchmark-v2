from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = 0
    anagrams = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s].append(s)
    for group in anagrams.values():
        anagram_count += len(group) * (len(group) - 1) // 2
        if anagram_count > 18:
            return False
    return True