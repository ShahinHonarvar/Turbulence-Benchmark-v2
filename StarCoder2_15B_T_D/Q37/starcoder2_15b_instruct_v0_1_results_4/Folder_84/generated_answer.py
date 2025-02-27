def filter_chars(string):
    chars_to_remove = [chr(i) for i in range(ord('6'), ord('A') + 1)]
    filtered_string = ''.join((c for c in string if c not in chars_to_remove or string.index(c) < 138 or string.index(c) > 920))
    return filtered_string