def return_n_greatest_chars(string_of_distinct_characters):
    sorted_list = sorted(string_of_distinct_characters, key=ord, reverse=True)
    return sorted_list[:79]