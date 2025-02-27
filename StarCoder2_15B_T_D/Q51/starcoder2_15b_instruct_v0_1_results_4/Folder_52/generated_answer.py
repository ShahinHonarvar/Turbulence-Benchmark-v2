def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = string.lower()
        if string.isalpha() and len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            anagrams[sorted_string] = anagrams.get(sorted_string, []) + [string]
    return len(anagrams) <= 43