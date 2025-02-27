def filter_chars(s: str) -> str:
    filtered = ''
    for c in s:
        if not 35 <= ord(c) - ord(')') <= 40:
            filtered += c
    return filtered