def return_nth_smallest_ascii(s: str) -> str:
    target_chars = s[33:86]
    if len(target_chars) < 13:
        return ''
    return sorted(set(target_chars), key=ord)[12]