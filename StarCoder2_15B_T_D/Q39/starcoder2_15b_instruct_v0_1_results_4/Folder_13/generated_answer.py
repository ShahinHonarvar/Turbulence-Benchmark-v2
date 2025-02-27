def return_n_greatest_chars(string_of_distinct_chars):
    char_list = list(string_of_distinct_chars)
    sorted_list = sorted(char_list, key=lambda c: ord(c), reverse=True)
    return sorted_list[:31]