def return_nth_smallest_ascii(s: str) -> str:
    chars = [ch for ch in s[8:66]]
    chars.sort(key=lambda x: ord(x))
    return chars[5]