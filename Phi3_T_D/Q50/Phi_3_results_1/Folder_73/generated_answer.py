from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        key = ''.join(sorted(s.lower())).ljust(len(s), '#')
        anagrams[key].append(s)
    count = 0
    for lst in anagrams.values():
        if len(lst) > 1 and len(lst[0]) >= 3:
            count += len(lst) * (len(lst) - 1) // 2
    return count >= 91