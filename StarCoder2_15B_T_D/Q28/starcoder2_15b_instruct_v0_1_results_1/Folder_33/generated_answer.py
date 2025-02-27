def return_nth_smallest_ascii(s: str) -> str:
    substring = s[22:75]
    sorted_chars = sorted(substring)
    return sorted_chars[11]