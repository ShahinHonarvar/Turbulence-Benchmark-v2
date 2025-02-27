def if_contains_anagrams(string_list):
    sorted_strings = [''.join(sorted(s.lower())) for s in string_list if len(s) >= 3]
    return sum((sorted_strings.count(s) - 1 for s in set(sorted_strings))) >= 98