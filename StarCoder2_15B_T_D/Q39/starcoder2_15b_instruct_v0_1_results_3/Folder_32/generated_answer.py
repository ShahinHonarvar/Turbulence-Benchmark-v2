def return_n_greatest_chars(string_of_distinct_chars):
    list_of_chars = list(string_of_distinct_chars)
    sorted_list_of_chars = sorted(list_of_chars, key=lambda x: ord(x), reverse=True)
    return sorted_list_of_chars[:8]