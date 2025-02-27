def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = ''.join((c for c in string.lower() if c.isalpha()))
        if len(string) >= 3:
            key = ''.join(sorted(string))
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
    return len(anagrams) <= 29