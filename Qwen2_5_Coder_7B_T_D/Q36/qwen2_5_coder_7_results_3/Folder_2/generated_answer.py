def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('D') + 1, ord('J'))]
    mask = [char not in target_chars for char in s[421:854]]
    return s[:421] + ''.join((char for char, keep in zip(s[421:854], mask) if keep)) + s[854:]