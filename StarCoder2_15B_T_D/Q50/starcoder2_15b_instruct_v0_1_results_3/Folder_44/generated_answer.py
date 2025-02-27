def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical = ''.join(sorted(string.lower()))
        if canonical not in anagrams:
            anagrams[canonical] = [string]
        else:
            anagrams[canonical].append(string)
    return any((len(group) >= 4 for group in anagrams.values()))