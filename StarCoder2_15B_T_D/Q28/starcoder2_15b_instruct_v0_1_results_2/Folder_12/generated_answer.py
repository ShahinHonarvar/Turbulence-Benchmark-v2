def return_nth_smallest_ascii(string: str) -> str:
    chars = [char for char in string[3:27]]
    chars.sort(key=lambda c: ord(c))
    return chars[4]