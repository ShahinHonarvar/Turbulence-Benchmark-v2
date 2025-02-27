def filter_chars(s):
    chars_to_remove = [chr(x) for x in range(ord('B'), ord('I'))]
    return ''.join([c for c in s if c not in chars_to_remove])