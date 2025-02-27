def filter_chars(s):
    start, end, step = (515, 538, 1)
    chars_to_remove = set()
    for i in range(start, end + 1):
        if '+' <= s[i] <= '}':
            chars_to_remove.add(s[i])
    return ''.join([char for char in s if char not in chars_to_remove])