def if_contains_anagrams(string_list):
    sorted_strings = [''.join(sorted(word.lower())) for word in string_list if len(word) >= 3]
    unique_sorted = set(sorted_strings)
    return len(sorted_strings) - len(unique_sorted) <= 474