def return_nth_smallest_ascii(s: str) -> str:
    chars_in_range = [c for i, c in enumerate(s) if 20 <= i <= 80]
    sorted_chars = sorted(chars_in_range, key=lambda c: ord(c))
    return sorted_chars[10]