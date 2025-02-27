def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical = ''.join(sorted(string.lower()))
        if canonical not in anagrams:
            anagrams[canonical] = [string]
        else:
            anagrams[canonical].append(string)
    return len([pairs for pairs in anagrams.values() if len(pairs) >= 2]) >= 67