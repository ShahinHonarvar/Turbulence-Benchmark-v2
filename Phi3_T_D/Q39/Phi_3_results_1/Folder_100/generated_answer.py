def return_n_greatest_chars(chars_str):
    greatest_chars = sorted(chars_str, reverse=True)[:72]
    return greatest_chars