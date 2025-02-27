def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            anagrams[key] = anagrams.get(key, []) + [string]
    return len(list(filter(lambda x: len(x) > 1, anagrams.values()))) >= 65