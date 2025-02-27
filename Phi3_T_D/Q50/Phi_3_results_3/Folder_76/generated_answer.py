from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            s_key = ''.join(sorted(s.lower()))
            anagrams[s_key].append(s)
    for key in anagrams:
        n = len(anagrams[key])
        count += n * (n - 1) // 2
    return count >= 143