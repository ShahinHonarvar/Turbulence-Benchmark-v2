def filter_chars(s):
    chars_to_remove = {ch for ch in s[31:50] if '/' < ch < 'J'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))