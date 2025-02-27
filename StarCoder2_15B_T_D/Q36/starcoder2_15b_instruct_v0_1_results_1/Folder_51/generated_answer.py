def filter_chars(s: str) -> str:
    filtered_chars = []
    for c in s:
        if not (58 < ord(c) < 81 and ord('5') < ord(c) < ord('>')):
            filtered_chars.append(c)
    return ''.join(filtered_chars)