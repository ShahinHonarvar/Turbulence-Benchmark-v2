def return_nth_smallest_ascii(s: str) -> str:
    chars = [c for c in s[47:81]]
    chars.sort(key=lambda c: ord(c))
    return chars[3]