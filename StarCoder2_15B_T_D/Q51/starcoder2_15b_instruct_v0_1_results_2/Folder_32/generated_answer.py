def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
    return len(anagrams) <= 89