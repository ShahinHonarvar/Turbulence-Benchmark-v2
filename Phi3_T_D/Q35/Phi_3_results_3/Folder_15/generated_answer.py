def remove_repeat_chars(s):
    unique_chars = set(s[0:5])
    return ''.join((ch for ch in s if ch not in unique_chars or unique_chars.pop() == ch))