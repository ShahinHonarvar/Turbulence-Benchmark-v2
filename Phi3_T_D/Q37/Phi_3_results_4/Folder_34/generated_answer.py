def filter_chars(s):
    chars_to_remove = [c for i, c in enumerate(s[54:62 + 1], start=54) if ')' <= c <= '9']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s