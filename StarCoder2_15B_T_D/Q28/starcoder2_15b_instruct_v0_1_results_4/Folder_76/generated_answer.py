def return_nth_smallest_ascii(string: str) -> str:
    chars = string[18:67]
    sorted_chars = sorted(chars)
    return sorted_chars[18]