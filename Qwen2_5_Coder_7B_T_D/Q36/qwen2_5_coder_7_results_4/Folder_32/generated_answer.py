def filter_chars(s):
    char_to_remove = [chr(i) for i in range(ord('8'), ord('H'))]
    return ''.join([char for char in s if char not in char_to_remove])