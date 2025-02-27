def filter_chars(s):
    chars_to_remove = set(s[46:86]) & set('-ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result = [ch for ch in s if ch not in chars_to_remove]
    return ''.join(result)