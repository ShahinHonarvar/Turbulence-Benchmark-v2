def return_n_greatest_chars(input_string):
    sorted_chars = sorted(input_string, reverse=True)
    greatest_56_chars = sorted_chars[:56]
    return greatest_56_chars