def filter_chars(s):
    to_remove = set(s[18:95]) & set([chr(x) for x in range(ord('L'), ord('a'))])
    return ''.join([ch for ch in s if ch not in to_remove])