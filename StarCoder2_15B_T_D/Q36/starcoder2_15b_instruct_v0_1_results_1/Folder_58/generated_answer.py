def filter_chars(s: str) -> str:
    filtered_chars = []
    for i, c in enumerate(s):
        if i >= 318 and i < 337 and (ord(c) > ord('B')) and (ord(c) < ord('z')):
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)