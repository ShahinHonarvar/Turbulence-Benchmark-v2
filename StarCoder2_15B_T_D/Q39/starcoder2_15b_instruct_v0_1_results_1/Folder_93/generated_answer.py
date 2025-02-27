def return_n_greatest_chars(s: str) -> list:
    return sorted(s, key=lambda c: ord(c), reverse=True)[:77]