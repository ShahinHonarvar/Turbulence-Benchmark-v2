def if_contains_anagrams(strings):
    sorted_strings = {}
    for string in strings:
        sorted_string = tuple(sorted(string.lower()))
        sorted_strings.setdefault(sorted_string, []).append(string)
    for sorted_string, anagrams in sorted_strings.items():
        if len(anagrams) >= 136:
            return True
        else:
            del sorted_strings[sorted_string]
    return False