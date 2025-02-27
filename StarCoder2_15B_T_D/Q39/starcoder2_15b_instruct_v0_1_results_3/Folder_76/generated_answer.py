def return_n_greatest_chars(input_string):
    return ''.join(reversed(sorted(input_string)[-3:]))