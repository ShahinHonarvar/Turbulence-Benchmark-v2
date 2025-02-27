def return_n_smallest_chars(string_of_distinct_chars):
    list_of_chars = list(string_of_distinct_chars)
    sorted_chars = sorted(list_of_chars, key=ord)
    return sorted_chars[:16][::-1]