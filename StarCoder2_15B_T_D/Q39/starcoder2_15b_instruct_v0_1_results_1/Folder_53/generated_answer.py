def return_n_greatest_chars(s):
    assert isinstance(s, str) and len(s) >= 19, 'Input should be a string of at least 19 distinct characters'
    assert all((len(set(c)) == 1 for c in s)), 'Input should be a string of distinct characters'
    sorted_s = sorted(s, key=lambda c: ord(c), reverse=True)
    return sorted_s[:19]