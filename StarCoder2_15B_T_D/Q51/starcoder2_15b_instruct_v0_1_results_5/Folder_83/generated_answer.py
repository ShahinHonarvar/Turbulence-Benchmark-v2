def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    return max(anagrams.values()) <= 19