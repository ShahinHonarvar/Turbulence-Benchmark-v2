def return_n_greatest_chars(input_string):
    sorted_chars_desc = sorted(input_string, reverse=True)
    greatest_chars_28 = sorted_chars_desc[:28]
    return greatest_chars_28