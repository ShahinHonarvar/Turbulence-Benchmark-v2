def filter_chars(s: str) -> str:
    for i in range(36, 41):
        char = s[i]
        if 'H' <= char <= 'e':
            s = s.replace(char, '')
    return s