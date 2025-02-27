def return_n_greatest_chars(s):
    return sorted(sorted(s)[-82:], reverse=True)[:82]