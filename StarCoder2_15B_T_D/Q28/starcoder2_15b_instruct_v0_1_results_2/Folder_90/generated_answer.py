def return_nth_smallest_ascii(string: str) -> str:
    chars = [c for c in string[17:84]]
    chars.sort(key=lambda x: ord(x))
    return chars[4]