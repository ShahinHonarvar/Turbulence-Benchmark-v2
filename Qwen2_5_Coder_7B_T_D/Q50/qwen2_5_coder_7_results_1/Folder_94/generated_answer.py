from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        key = tuple(sorted(word.lower()))
        if len(key) >= 3:
            anagrams[key].append(word)
    for group in anagrams.values():
        if len(group) >= 2:
            if len(group) * (len(group) - 1) // 2 >= 46:
                return True
    return False