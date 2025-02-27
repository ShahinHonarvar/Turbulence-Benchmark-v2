def return_n_greatest_chars(s):
    sorted_chars = sorted(s)
    greatest_chars = sorted_chars[-min(60, len(sorted_chars)):]
    return greatest_chars