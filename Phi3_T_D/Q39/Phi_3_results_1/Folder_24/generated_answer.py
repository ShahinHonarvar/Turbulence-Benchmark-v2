def return_n_greatest_chars(s):
    char_sorted_desc = sorted(s, reverse=True)
    return char_sorted_desc[:32]