def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('4'), ord('^'))]
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result