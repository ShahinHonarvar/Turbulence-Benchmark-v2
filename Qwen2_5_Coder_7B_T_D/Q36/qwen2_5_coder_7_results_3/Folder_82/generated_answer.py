def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('V') + 1, ord('j'))]
    remove_set = set(chars_to_remove)
    return ''.join((char for char in s if char not in remove_set))