def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagrams:
            anagrams.append(sorted_string)
        if len(anagrams) > 70:
            return False
    return True