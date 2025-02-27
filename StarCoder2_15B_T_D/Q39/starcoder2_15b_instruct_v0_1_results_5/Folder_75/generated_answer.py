def return_n_greatest_chars(s: str) -> list:
    if not s or len(s) < 2:
        raise ValueError('The input string must have at least 2 distinct characters')
    sorted_chars = sorted(s)
    return sorted_chars[-2:]