def filter_chars(s):
    start, end = (11, 72)
    target_range = s[start - 1:end]
    filtered_chars = ''.join([char for char in target_range if ord('i') <= ord(char) <= ord('v')])
    for char in filtered_chars:
        s = s.replace(char, '')
    return s