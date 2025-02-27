def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if key not in anagrams:
            anagrams[key] = [string]
        else:
            anagrams[key].append(string)
    count = 0
    for key in anagrams.keys():
        if len(anagrams[key]) >= 2 and len(anagrams[key][0]) >= 3:
            count += len(anagrams[key]) // 2
    return count >= 140