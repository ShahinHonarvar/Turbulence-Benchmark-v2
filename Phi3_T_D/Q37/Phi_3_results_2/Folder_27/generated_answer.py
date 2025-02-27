def filter_chars(s):
    start, end = (43, 80)
    chars_to_remove = [c for c in s[start:end + 1] if '=' <= c <= 'E']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s