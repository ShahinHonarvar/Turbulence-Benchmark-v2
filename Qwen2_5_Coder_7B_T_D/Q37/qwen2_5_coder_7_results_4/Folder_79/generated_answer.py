def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(ord('@'), ord('T') + 1)])
    result = ''.join([char for char in s if 10 <= s.index(char) <= 52 and char not in chars_to_remove])
    return result