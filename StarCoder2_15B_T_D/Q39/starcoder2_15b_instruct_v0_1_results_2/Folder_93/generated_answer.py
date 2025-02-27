def return_n_greatest_chars(s: str) -> list:
    assert len(s) >= 77, 'Input string must be at least 77 characters long'
    assert len(set(s)) == len(s), 'Input string must contain distinct characters'
    char_list = list(s)
    char_list.sort(key=lambda c: ord(c), reverse=True)
    return char_list[:77]