def remove_repeat_chars(s):
    return ''.join((c for i, c in enumerate(s) if s[i + 1:i + 3].count(c) == 0 and s[:i].count(c) == 0))