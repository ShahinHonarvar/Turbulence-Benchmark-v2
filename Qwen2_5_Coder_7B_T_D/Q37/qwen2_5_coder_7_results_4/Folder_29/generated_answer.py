def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('&'), ord('v') + 1)))
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result