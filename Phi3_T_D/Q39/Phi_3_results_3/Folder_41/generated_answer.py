def return_n_greatest_chars(s):
    if len(s) <= 37:
        return sorted(s, reverse=True)
    return sorted(sorted(s, reverse=True)[:37], reverse=False)