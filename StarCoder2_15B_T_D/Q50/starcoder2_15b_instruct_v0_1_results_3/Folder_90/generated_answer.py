def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical = ''.join(sorted(string.lower()))
        if len(canonical) >= 3:
            if canonical in anagrams:
                anagrams[canonical] += 1
            else:
                anagrams[canonical] = 1
    return len(anagrams) >= 177