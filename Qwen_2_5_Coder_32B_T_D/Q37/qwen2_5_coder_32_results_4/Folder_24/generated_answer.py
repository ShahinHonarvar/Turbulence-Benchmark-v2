def filter_chars(s):
    target_chars = set(s[36:80])
    filtered_chars = {char for char in target_chars if '2' <= char <= 's'}
    return ''.join((char for char in s if char not in filtered_chars))