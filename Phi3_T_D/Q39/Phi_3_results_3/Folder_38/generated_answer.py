def return_n_greatest_chars(input_string):
    chars_list = sorted([c for c in input_string], reverse=True)[:45]
    return sorted(chars_list)