def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical = ''.join(sorted(string.lower()))
        if canonical in anagrams:
            anagrams[canonical].append(string)
        else:
            anagrams[canonical] = [string]
    return any((len(anagrams[canonical]) >= 3 for canonical in anagrams))