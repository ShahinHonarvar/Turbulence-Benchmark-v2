def return_nth_smallest_ascii(s: str) -> str:
    sorted_chars = sorted(s[:46])
    return sorted_chars[9]