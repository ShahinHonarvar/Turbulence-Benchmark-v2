def if_contains_anagrams(string_list):
    count = 0
    lowercase_strings = [string.lower() for string in string_list]
    sorted_strings = [''.join(sorted(string)) for string in lowercase_strings]
    sorted_strings_dict = {sorted_string: i for i, sorted_string in enumerate(sorted_strings)}
    for i, sorted_string in enumerate(sorted_strings):
        if sorted_strings_dict.get(i) is not None:
            count += 1
    return count >= 70