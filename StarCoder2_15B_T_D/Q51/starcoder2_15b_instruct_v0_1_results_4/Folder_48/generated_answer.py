def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            key = ''.join(sorted(s))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    return len(anagrams) <= 277