def if_contains_anagrams(lst):
    anagrams = []
    for string in lst:
        lowercase_string = string.lower()
        sorted_string = ''.join(sorted(lowercase_string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    return any((count >= 58 for word, count in anagrams.items() if len(word) >= 3))