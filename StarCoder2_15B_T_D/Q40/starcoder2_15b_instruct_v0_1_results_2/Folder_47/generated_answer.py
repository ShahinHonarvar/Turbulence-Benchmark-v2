def return_n_smallest_chars(string_of_distinct_characters):
    char_list = list(string_of_distinct_characters)
    char_list.sort(key=lambda c: ord(c))
    return char_list[-21:]