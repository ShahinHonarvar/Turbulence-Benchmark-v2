def filter_chars(s):
    char_to_remove = [chr(i) for i in range(ord('i'), ord('k'))]
    result = ''.join([char for char in s if char not in char_to_remove])
    return result