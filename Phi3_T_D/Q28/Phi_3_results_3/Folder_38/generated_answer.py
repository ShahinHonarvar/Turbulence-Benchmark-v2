def return_nth_smallest_ascii(s: str) -> str:
    selected_chars = sorted(s[0:46])
    return selected_chars[9] if len(selected_chars) > 9 else ''