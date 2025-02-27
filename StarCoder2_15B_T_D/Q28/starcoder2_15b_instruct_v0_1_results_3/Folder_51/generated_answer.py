def return_nth_smallest_ascii(s: str) -> str:
    chars = [ch for ch in s[10:74]]
    chars.sort(key=lambda c: ord(c))
    return chars[8]