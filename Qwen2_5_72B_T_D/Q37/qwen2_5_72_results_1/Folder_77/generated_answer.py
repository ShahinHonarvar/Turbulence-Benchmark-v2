def filter_chars(s):
    chars_to_remove = set([s[i] for i in range(384, 412) if 384 <= i < len(s) and '/' <= s[i] <= '8'])
    return ''.join([ch for ch in s if ch not in chars_to_remove])