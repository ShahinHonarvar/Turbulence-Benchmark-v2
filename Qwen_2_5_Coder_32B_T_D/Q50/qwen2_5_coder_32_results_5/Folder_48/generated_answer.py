from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    anagrams = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            s = ''.join(sorted(s))
            anagrams[s] += 1
            count += anagrams[s] - 1
            if count >= 219:
                return True
    return False