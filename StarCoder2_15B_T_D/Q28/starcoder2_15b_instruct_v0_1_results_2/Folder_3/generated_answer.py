def return_nth_smallest_ascii(s: str) -> str:
    chars_between_indices = [char for i, char in enumerate(s) if 25 <= i <= 45]
    sorted_chars = sorted(chars_between_indices, key=lambda char: ord(char))
    return sorted_chars[10]