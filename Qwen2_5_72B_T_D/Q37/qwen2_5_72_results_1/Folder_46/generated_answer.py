def filter_chars(s):
    chars_to_remove = set((char for char in s[11:73] if 'i' <= char <= 'v'))
    return ''.join((char for char in s if char not in chars_to_remove))