def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    return len(strings) - sum(anagrams.values()) <= 6