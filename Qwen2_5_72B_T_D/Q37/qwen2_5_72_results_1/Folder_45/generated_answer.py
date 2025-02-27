def filter_chars(s):
    chars_to_remove = set()
    for i in range(72, 95):
        if 72 <= i <= 94 and '.' <= s[i] <= 'b':
            chars_to_remove.add(s[i])
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result