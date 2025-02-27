def return_n_greatest_chars(chars):
    assert len(set(chars)) == len(chars), 'The string must consist of distinct characters.'
    if len(chars) <= 5:
        return sorted(chars)
    return sorted(chars)[len(chars) - 55:]