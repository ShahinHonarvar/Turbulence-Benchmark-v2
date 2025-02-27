def return_n_greatest_chars(chars):
    if len(chars) < 3:
        return sorted(chars, reverse=True)
    else:
        return sorted(chars, reverse=True)[:3]