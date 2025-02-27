def remove_repeat_chars(s):
    new_str = [c for i, c in enumerate(s) if i < 25 or 80 < i or s[i] != s[i - 25:i + 20].count(c) > 1]
    return ''.join(new_str)