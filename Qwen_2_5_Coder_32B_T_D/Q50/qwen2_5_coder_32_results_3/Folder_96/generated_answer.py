from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagrams = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            key = ''.join(sorted(s_lower))
            anagrams[key].append(s_lower)
    for a in anagrams.values():
        n = len(a)
        if n > 1:
            count += n * (n - 1) // 2
            if count >= 98:
                return True
    return False