def filter_chars(s):
    out = [''] * len(s)
    remove = set((chr(i) for i in range(ord('K'), ord(']') + 1)))
    for i, char in enumerate(s):
        if 41 <= i <= 64 and char in remove:
            continue
        out[i] = char
    return ''.join(out)