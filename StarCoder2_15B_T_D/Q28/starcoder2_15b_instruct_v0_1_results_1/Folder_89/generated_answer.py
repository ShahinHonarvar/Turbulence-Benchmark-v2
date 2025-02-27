def return_nth_smallest_ascii(s: str) -> str:
    chars = [c for c in s[24:72]]
    chars.sort(key=lambda c: ord(c))
    return chars[7]