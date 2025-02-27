def if_contains_anagrams(strings):
    unique_strings = set()
    for string in strings:
        normalized_string = normalize(string)
        unique_strings.add(normalized_string)
    return len(unique_strings) <= 97

def normalize(string):
    return ''.join(sorted(string.lower()))