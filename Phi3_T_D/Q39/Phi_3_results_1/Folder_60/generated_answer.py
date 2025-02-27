def return_n_greatest_chars(s):
    if len(s) > 28:
        sorted_chars = sorted(s, reverse=True)
        return sorted_chars[:28]
    else:
        return sorted(s, reverse=True)