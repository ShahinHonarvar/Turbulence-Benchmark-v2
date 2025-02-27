def filter_chars(s: str) -> str:
    filtered_chars = []
    for c in s:
        if not (513 <= ord(c) <= 877 and ord('?') <= ord(c) <= ord('n')):
            filtered_chars.append(c)
    return ''.join(filtered_chars)