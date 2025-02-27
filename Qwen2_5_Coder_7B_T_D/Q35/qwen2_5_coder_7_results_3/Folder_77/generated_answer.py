def remove_repeat_chars(s):
    return s[:355] + ''.join((ch for i, ch in enumerate(s[355:988]) if s[355:988].count(ch) == 1)) + s[988:]