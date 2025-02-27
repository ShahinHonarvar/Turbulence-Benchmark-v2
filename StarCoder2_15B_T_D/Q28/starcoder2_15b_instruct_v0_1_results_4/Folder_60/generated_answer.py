def return_nth_smallest_ascii(s: str) -> str:
    filtered_chars = [c for i, c in enumerate(s) if 36 <= i <= 79]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[11]