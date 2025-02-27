def filter_chars(s):
    char_to_remove = [chr(i) for i in range(ord('h') + 1, ord('k'))]
    remove_set = set(char_to_remove)
    return ''.join([char for char in s if char not in remove_set])