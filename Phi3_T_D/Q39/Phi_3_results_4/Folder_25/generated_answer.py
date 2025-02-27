def return_n_greatest_chars(input_string):
    greatest_chars = sorted(input_string, reverse=True)[:29]
    return greatest_chars