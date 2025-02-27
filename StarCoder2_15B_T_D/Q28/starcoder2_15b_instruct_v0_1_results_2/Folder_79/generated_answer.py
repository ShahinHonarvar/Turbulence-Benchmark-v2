def return_nth_smallest_ascii(s: str) -> str:
    chars = list(s[13:36])
    chars.sort(key=lambda c: ord(c))
    return chars[17]