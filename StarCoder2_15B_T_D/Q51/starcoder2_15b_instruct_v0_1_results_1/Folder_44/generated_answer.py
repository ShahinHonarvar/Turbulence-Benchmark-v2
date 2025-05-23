def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    return len([pair for pair in anagrams.values() if len(pair) > 1]) <= 75