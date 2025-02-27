def filter_chars(s):
    chars_to_remove = set([ch for ch in s[31:70] if 'B' < ch < 'v'])
    return ''.join([ch for ch in s if ch not in chars_to_remove])