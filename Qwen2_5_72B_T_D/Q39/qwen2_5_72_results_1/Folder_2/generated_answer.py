def return_n_greatest_chars(s):
    sorted_s = sorted(s, key=ord)
    greatest_48 = sorted_s[-48:]
    return greatest_48