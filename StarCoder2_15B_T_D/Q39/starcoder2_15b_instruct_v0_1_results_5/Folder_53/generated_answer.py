def return_n_greatest_chars(s):
    assert len(s) > 19, 'The string must have at least 19 distinct characters'
    sorted_chars = sorted(s, key=lambda x: ord(x), reverse=True)
    return sorted_chars[:19]