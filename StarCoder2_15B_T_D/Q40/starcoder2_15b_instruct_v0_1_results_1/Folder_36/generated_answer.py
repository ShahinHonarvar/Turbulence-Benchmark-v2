def return_n_smallest_chars(string_of_distinct_chars):
    char_list = list(string_of_distinct_chars)
    char_list.sort()
    return char_list[:32]