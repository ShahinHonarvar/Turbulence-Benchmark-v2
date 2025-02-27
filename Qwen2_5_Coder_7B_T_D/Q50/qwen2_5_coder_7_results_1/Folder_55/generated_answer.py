from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[sorted_s].append(s)
    for group in anagrams.values():
        if len(group) >= 2:
            return True
    return False