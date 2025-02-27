def filter_chars(s: str) -> str:
    filtered_chars = []
    for c in s:
        if 24 <= ord(c) - ord('a') <= 55 and ord('a') <= ord(c) <= ord('f'):
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)