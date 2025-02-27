def return_n_greatest_chars(input_str):
    if len(input_str) <= 44:
        char_list = list(input_str)
    else:
        char_list = sorted(list(input_str), reverse=True)[:44]
    return char_list