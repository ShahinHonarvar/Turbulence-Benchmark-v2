def return_n_greatest_chars(s):
    if len(s) < 82:
        return sorted(s, reverse=True)
    else:
        return sorted(s, reverse=True)[:82]