def filter_chars(s):
    keep_chars = set(range(ord('0'), ord('@') + 1))
    return ''.join((char for i, char in enumerate(s) if i < 61 or i > 70 or ord(char) not in keep_chars))