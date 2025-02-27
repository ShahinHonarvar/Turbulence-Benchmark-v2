def filter_chars(s: str) -> str:
    filtered_chars = []
    for c in s:
        if c >= '5' and c <= '<' and (s.index(c) >= 24 and s.index(c) <= 82):
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)