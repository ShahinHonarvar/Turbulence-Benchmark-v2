def filter_chars(s: str) -> str:
    filtered_chars = []
    for c in s:
        if not 46 < ord(c) < 68 or not ord('H') < ord(c) < ord('s'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)