def filter_chars(s):
    chars_to_remove = set()
    for i in range(379, 899):
        if 379 <= i <= 898 and 'M' <= s[i] <= 'v':
            chars_to_remove.add(s[i])
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result