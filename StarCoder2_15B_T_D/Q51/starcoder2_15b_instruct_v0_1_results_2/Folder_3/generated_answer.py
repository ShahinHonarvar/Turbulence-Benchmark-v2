def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        canonical = ''.join(sorted(string.lower()))
        anagrams[canonical] = anagrams.get(canonical, 0) + 1
    return len(anagrams) <= 66