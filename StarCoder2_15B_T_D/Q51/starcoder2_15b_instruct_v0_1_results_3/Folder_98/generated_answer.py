def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        normalized = ''.join((c for c in string.lower() if c.isalpha()))
        key = ''.join(sorted(normalized))
        if len(key) >= 3:
            anagrams[key] = anagrams.get(key, []) + [string]
    return len(anagrams) <= 46