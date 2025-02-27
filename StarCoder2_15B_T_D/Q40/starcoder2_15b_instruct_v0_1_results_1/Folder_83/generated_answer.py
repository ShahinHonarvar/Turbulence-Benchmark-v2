def return_n_smallest_chars(s):
    assert len(set(s)) == len(s), 'The string must contain distinct characters'
    assert len(s) >= 38, 'The string must be at least 38 characters long'
    sorted_chars = sorted(s, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:38]