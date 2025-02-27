def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(ord('D'), ord('Y') + 1)])
    return ''.join([char for char in s if not (225 <= s.index(char) <= 381 and char in chars_to_remove)])