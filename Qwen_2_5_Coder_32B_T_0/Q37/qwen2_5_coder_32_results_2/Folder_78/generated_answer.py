def filter_chars(s):
    chars_to_remove = set(s[75:100]) & set('89:;<=>?@ABCDEFG')
    return ''.join((c for c in s if c not in chars_to_remove))