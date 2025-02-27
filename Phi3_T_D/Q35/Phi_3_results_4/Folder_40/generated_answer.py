def remove_repeat_chars(s):
    seen_chars = set()
    out_chars = []
    for i in range(1, 4):
        char = s[i]
        if char not in seen_chars:
            seen_chars.add(char)
            out_chars.append(char)
    return ''.join(out_chars)