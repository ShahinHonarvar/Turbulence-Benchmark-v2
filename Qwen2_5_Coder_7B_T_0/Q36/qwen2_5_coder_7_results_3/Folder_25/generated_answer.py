def filter_chars(s):
    chars_to_remove = set()
    for i in range(24, 37):
        if 'A' < s[i] < 'h':
            chars_to_remove.add(s[i])
    return ''.join([char for char in s if char not in chars_to_remove])