def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = ''.join((c for c in string.lower() if c.isalpha()))
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    return max(anagrams.values(), default=0) <= 21