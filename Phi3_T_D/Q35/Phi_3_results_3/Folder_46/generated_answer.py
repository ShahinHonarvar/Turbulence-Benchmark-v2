def remove_repeat_chars(s):
    s = s[10:79].replace('\\\\b(\\\\w)(\\\\w*\\\\1)\\\\b', '') + s[79:]
    return s