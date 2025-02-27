def return_n_greatest_chars(s):
    assert len(s) == 26, 'Input must be a string of 26 distinct characters'
    return sorted(s, key=ord, reverse=True)