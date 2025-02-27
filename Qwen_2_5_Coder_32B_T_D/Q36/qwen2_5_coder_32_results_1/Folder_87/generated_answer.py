def filter_chars(s):
    chars_to_remove = set(s[32:61]) & set([chr(i) for i in range(ord('4'), ord('D'))])
    return ''.join([ch for ch in s if ch not in chars_to_remove])