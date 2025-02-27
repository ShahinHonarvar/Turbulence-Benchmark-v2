def return_n_greatest_chars(string):
    assert len(set(string)) == len(string), 'The given string should contain distinct characters.'
    return sorted(string, key=ord, reverse=True)[:84]