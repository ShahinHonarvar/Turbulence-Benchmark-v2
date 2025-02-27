from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        key = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            d[key].append(word)
    count = 0
    for v in d.values():
        if len(v) > 1:
            count += len(v) * (len(v) - 1) // 2
    return count >= 35