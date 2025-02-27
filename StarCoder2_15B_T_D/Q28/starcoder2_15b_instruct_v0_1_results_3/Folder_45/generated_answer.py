def return_nth_smallest_ascii(s: str) -> str:
    assert len(s) >= 16, 'The input string must have at least 16 characters.'
    chars = sorted(s[:16])
    return chars[15]