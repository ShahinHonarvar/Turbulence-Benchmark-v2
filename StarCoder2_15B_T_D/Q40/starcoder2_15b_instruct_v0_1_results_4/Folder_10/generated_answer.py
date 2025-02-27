def return_n_smallest_chars(string):
    assert len(set(string)) == len(string), 'The input string must contain distinct characters.'
    sorted_chars = sorted(string, key=lambda c: ord(c))
    return sorted_chars[-88:]