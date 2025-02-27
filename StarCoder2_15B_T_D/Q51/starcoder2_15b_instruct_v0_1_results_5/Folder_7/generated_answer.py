def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = string.lower()
        key = ''.join(sorted(string))
        if len(string) >= 3:
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
    num_anagrams = sum((len(anagrams[key]) - 1 for key in anagrams if len(anagrams[key]) > 1))
    return num_anagrams <= 445