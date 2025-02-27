def return_nth_smallest_ascii(string: str) -> str:
    filtered_chars = [ch for ch in string[7:65] if ch.isalpha()]
    sorted_chars = sorted(filtered_chars, key=lambda ch: ord(ch))
    return sorted_chars[5]