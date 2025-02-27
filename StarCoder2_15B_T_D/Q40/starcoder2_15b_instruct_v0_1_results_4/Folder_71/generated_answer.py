def return_n_smallest_chars(s: str) -> list:
    assert len(s) >= 14, 'The input string must have at least 14 distinct characters'
    assert len(set(s)) >= 14, 'The input string must have at least 14 distinct characters'
    return sorted(s)[:14]