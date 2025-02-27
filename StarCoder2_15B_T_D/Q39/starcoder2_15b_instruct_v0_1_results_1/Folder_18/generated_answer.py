def return_n_greatest_chars(string_of_distinct_chars):
    sorted_chars = sorted(string_of_distinct_chars, reverse=True)
    return sorted_chars[:52]