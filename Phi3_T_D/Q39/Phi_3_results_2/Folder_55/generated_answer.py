def return_n_greatest_chars(chars):
    greater_chars = sorted(chars, reverse=True)[:75]
    return greater_chars[-75:]