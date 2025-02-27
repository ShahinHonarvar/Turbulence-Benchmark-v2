def if_contains_anagrams(strings):
    anagrams = {}
    for i, string in enumerate(strings):
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key].append(i)
        else:
            anagrams[key] = [i]
    return len([key for key in anagrams if len(anagrams[key]) >= 28]) > 0