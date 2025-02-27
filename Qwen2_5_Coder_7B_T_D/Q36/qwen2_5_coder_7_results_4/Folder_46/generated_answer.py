def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('<') + 1, ord('C'))]
    remove_set = set(chars_to_remove)
    result = ''.join((char for char in s if char not in remove_set))
    return result