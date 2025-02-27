from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    anagrams = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] += 1
            count += anagrams[sorted_s] - 1
            if count >= 14:
                return True
    return False