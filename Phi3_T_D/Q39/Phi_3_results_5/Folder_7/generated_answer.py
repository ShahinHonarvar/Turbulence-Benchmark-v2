def return_n_greatest_chars(chars):
    if len(chars) != 49:
        raise ValueError('The input must be a string of exactly 49 distinct characters')
    return sorted(chars, reverse=True)