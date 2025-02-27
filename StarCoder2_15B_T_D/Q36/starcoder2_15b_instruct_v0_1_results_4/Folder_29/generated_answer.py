def filter_chars(text: str) -> str:
    ascii_H = ord('H')
    ascii_s = ord('s')
    filtered_chars = []
    for c in text:
        ascii_c = ord(c)
        if not ascii_H < ascii_c < ascii_s:
            filtered_chars.append(c)
    return ''.join(filtered_chars)