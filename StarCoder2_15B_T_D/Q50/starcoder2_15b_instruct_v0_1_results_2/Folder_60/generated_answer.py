def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            key = ''.join(sorted(s_lower))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    return len(anagrams) >= 60