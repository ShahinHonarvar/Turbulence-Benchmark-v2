def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    return max(anagrams.values()) <= 9