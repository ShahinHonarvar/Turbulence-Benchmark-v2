def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        key = ''.join(sorted(s_lower))
        if len(s_lower) >= 3:
            anagrams[key] = anagrams.get(key, []) + [s]
    return len(anagrams) >= 36