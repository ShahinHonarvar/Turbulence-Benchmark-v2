def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if key not in anagrams:
            anagrams[key] = [string]
        else:
            anagrams[key].append(string)
    num_anagrams = sum((len(v) - 1 for v in anagrams.values()))
    return num_anagrams <= 131