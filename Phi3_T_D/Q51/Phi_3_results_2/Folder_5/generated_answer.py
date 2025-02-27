def if_contains_anagrams(str_list):
    sorted_strings_dict = {}
    anagrams_count = 0
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in sorted_strings_dict:
            sorted_strings_dict[sorted_string] += 1
            if sorted_strings_dict[sorted_string] == 2:
                anagrams_count += 1
        else:
            sorted_strings_dict[sorted_string] = 1
    return anagrams_count <= 4