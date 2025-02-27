def return_n_greatest_chars(s):
    return sorted(s, key=ord)[-3:][::-1]