def return_n_greatest_chars(input_string):
    char_list = sorted(input_string, reverse=True)[:27]
    return char_list