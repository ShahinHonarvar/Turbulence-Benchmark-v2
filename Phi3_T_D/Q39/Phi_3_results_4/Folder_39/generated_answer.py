def return_n_greatest_chars(s):
    sorted_chars = sorted(s)
    greatest_chars = sorted_chars[-23:]
    return greatest_chars