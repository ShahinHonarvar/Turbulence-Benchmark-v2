def return_nth_smallest_ascii(s: str) -> str:
    sorted_chars = sorted(s[:10])
    return sorted_chars[9]