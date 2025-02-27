def return_nth_smallest_ascii(s: str) -> str:
    filtered = [c for i, c in enumerate(s) if 1 <= i <= 46]
    sorted_chars = sorted(filtered, key=lambda c: ord(c))
    return sorted_chars[12]