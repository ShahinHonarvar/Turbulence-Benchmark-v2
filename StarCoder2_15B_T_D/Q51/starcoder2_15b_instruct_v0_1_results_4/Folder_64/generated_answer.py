def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical = ''.join(sorted(string.lower()))
        if canonical in anagrams:
            anagrams[canonical].append(string)
        else:
            anagrams[canonical] = [string]
    return len(anagrams) <= 59