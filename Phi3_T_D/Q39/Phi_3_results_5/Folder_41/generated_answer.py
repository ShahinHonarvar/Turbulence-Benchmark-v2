def return_n_greatest_chars(chars):
    if len(chars) > 37:
        sorted_chars = sorted(chars, reverse=True)[:37]
    else:
        sorted_chars = sorted(chars, reverse=True)
    return sorted_chars