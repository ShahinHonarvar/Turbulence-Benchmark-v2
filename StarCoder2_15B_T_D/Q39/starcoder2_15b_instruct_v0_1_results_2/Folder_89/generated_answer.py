def return_n_greatest_chars(string_of_distinct_chars):
    char_list = list(string_of_distinct_chars)
    char_list.sort(key=lambda c: ord(c), reverse=True)
    return char_list[:55]