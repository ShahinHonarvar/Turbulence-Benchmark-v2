def filter_chars(s):
    if len(s) <= 411:
        chars_to_remove = set(s[max(384, len(s) - 1):412])
    else:
        chars_to_remove = set(s[384:412])
    chars_to_remove = {char for char in chars_to_remove if '/' <= char <= '8'}
    return ''.join((char for char in s if char not in chars_to_remove))