def return_n_greatest_chars(s):
    if len(s) <= 56:
        return sorted(s, reverse=True)
    else:
        return sorted(s, reverse=True)[:56]