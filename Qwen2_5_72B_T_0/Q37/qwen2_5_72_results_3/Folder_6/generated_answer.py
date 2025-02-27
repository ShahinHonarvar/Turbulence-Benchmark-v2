def filter_chars(s):
    chars_to_remove = set()
    for i in range(13, 29):
        if 13 <= i <= 28 and 'c' <= s[i] <= 'n':
            chars_to_remove.add(s[i])
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result