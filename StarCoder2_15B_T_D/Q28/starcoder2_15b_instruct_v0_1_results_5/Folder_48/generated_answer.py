def return_nth_smallest_ascii(s: str) -> str:
    relevant_chars = [c for i, c in enumerate(s) if 37 <= i <= 59]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[5]