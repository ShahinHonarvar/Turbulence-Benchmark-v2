def return_n_greatest_chars(string_of_distinct_characters):
    sorted_characters = sorted(string_of_distinct_characters, key=ord)
    return sorted_characters[:21]