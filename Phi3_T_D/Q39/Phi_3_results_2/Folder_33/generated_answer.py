def return_n_greatest_chars(s):
    distinct_chars = sorted(set(s), key=ord, reverse=True)
    assert len(distinct_chars) <= 36, 'The string does not contain enough distinct characters'
    return distinct_chars[:36]