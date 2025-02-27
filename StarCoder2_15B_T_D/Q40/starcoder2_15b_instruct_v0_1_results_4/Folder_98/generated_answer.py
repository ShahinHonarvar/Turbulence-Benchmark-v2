def return_n_smallest_chars(string_of_distinct_characters):
    list_of_characters = list(string_of_distinct_characters)
    list_of_characters.sort()
    return list_of_characters[-68:]