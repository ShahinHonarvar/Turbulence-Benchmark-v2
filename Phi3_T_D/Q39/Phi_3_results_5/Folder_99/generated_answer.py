def return_n_greatest_chars(s):
    if len(s) <= 35:
        return sorted(s, reverse=True)
    elif len(s) > 35:
        return sorted(s, reverse=True)[:35]