def return_n_greatest_chars(input_string):
    sorted_string = sorted(input_string, reverse=True)
    return sorted_string[:64]