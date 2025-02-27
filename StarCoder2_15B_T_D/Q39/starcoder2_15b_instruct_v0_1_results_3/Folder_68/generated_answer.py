def return_n_greatest_chars(string_of_distinct_chars):
    sorted_list = sorted(string_of_distinct_chars, key=lambda x: ord(x), reverse=True)
    return sorted_list[:89]