def return_n_greatest_chars(input_string):
    sorted_chars = sorted(input_string)
    return sorted_chars[-64:]