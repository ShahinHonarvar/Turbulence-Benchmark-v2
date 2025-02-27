def return_nth_smallest_ascii(s: str) -> str:
    n = 16
    sorted_chars = sorted(s[:16])
    return sorted_chars[n - 1]