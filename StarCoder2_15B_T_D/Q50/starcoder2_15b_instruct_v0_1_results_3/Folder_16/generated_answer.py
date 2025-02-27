def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    return len(anagrams) >= 155