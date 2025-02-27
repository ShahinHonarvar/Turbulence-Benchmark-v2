def filter_chars(s):
    remove_chars = set((chr(i) for i in range(ord('*'), ord('b') + 1) if i >= ord('*') and i <= ord('b')))
    i = 42
    while i <= 97 and i < len(s):
        if s[i] in remove_chars:
            s = s[:i] + s[i + 1:]
        else:
            i += 1
    return s