def return_n_greatest_chars(s: str) -> str:
    return ''.join(sorted(s, key=lambda c: ord(c), reverse=True))[:85]