def return_nth_smallest_ascii(string: str) -> str:
    chars = [c for c in string if c in string[0:7]]
    chars.sort(key=lambda c: ord(c))
    return chars[6]