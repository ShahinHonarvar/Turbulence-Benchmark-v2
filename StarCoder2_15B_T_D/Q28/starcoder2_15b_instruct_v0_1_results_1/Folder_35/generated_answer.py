def return_nth_smallest_ascii(s: str) -> str:
    filtered_chars = [c for i, c in enumerate(s) if 50 <= i <= 75]
    sorted_chars = sorted(filtered_chars, key=lambda c: ord(c))
    return sorted_chars[6]