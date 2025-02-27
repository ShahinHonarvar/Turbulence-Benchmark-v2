def return_n_greatest_chars(string_of_distinct_chars):
    sorted_list = sorted(string_of_distinct_chars, key=ord, reverse=True)
    return sorted_list[:11]