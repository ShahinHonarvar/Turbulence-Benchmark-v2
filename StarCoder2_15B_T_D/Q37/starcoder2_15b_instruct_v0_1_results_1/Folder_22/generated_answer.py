def filter_chars(s: str) -> str:
    chars = list(s)
    filtered_chars = []
    for i, c in enumerate(chars):
        if 33 <= i <= 70 and '7' <= c <= 'k':
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)