def return_nth_smallest_ascii(string: str) -> str:
    chars = [char for char in string[35:53]]
    chars.sort(key=lambda c: ord(c))
    return chars[9]