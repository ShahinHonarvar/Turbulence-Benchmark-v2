def return_nth_smallest_ascii(s: str) -> str:
    characters = s[42:60]
    ascii_values = [ord(c) for c in characters]
    ascii_values.sort()
    return chr(ascii_values[16])