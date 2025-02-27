def return_n_greatest_chars(s):
    chars_sorted = sorted(s, key=ord, reverse=True)[:80]
    return chars_sorted