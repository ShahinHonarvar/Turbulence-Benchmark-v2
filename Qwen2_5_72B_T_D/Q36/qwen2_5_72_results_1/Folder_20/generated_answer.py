def filter_chars(s):
    chars_to_remove = set([ch for ch in s[13:40] if ':' < ch < 'C'])
    return ''.join([ch for ch in s if ch not in chars_to_remove])