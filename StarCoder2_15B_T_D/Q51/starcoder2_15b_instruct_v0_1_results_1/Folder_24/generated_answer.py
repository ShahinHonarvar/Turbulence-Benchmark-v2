def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in anagrams:
            anagrams.append(sorted_string)
    return len(anagrams) <= 96