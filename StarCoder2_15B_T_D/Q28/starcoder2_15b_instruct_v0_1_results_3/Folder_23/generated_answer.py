def return_nth_smallest_ascii(s: str) -> str:
    chars = [c for c in s if c.isalpha()]
    chars.sort(key=lambda c: ord(c))
    return chars[6]