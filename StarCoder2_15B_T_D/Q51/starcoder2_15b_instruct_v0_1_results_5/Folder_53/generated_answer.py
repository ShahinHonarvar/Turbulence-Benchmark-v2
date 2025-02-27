def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical = ''.join(sorted(string.lower()))
        if canonical not in anagrams:
            anagrams[canonical] = [string]
        else:
            anagrams[canonical].append(string)
    return len([group for group in anagrams.values() if len(group) > 1]) <= 8