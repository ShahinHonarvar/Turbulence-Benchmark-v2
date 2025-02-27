def return_n_greatest_chars(string_of_distinct_characters):
    list_of_chars = list(string_of_distinct_characters)
    sorted_list_of_chars = sorted(list_of_chars, key=lambda c: ord(c), reverse=True)
    return sorted_list_of_chars[:88]