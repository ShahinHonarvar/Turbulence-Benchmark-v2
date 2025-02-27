def filter_chars(s):
    chars_to_remove = set()
    for i in range(309, 591):
        if 309 <= i < len(s) and 'S' < s[i] < 'm':
            chars_to_remove.add(s[i])
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result