def return_n_smallest_chars(chars):
    if len(chars) < 72:
        chars *= -(-72 // len(chars))
    smallest_chars = sorted(chars)[:72]
    return sorted(smallest_chars, reverse=True)