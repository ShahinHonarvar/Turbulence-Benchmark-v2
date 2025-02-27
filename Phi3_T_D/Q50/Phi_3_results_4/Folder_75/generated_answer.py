from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    length_cutoff = 3
    for s in strings:
        if len(s) >= length_cutoff:
            sort_s = ''.join(sorted(s.lower()))
            anagrams[sort_s] += 1
            if anagrams[sort_s] >= 2:
                return True
    return False