def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if key not in anagrams:
            anagrams[key] = [string]
        else:
            anagrams[key].append(string)
    for key in anagrams.keys():
        if len(anagrams[key]) >= 3:
            return True
    return False