def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical = ''.join(sorted(string.lower()))
        if canonical not in anagrams:
            anagrams[canonical] = [string]
        else:
            anagrams[canonical].append(string)
    return any((len(v) >= 2 for v in anagrams.values()))