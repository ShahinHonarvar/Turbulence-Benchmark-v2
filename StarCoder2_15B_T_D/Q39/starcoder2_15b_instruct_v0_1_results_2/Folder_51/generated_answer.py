def return_n_greatest_chars(s: str) -> list:
    assert len(s) >= 45, 'The input string must contain at least 45 distinct characters.'
    chars = list(s)
    chars.sort(reverse=True)
    return chars[:45]