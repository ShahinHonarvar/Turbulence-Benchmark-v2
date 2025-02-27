def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    return any((len(anagrams[key]) >= 2 for key in anagrams if len(key) >= 3))