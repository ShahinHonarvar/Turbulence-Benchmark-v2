def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        key = ''.join(sorted(s))
        if len(s) >= 3:
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    return len(anagrams) <= 407