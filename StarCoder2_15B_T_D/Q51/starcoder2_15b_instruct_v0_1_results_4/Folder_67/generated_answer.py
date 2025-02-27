def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = string.lower()
        key = ''.join(sorted(string))
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    return len([pair for pair in anagrams.values() if len(pair) > 1]) <= 5