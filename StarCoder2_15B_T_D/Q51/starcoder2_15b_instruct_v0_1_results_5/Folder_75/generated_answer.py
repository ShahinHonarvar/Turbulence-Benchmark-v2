def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if s.isalpha() and len(s) >= 3:
            key = ''.join(sorted(s))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    return len(anagrams) <= 55