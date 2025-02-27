def filter_chars(string):
    chars_to_remove = {chr(i) for i in range(ord('7'), ord('e') + 1)}
    filtered_string = ''.join((c for c in string if c not in chars_to_remove or string.index(c) < 22 or string.index(c) > 85))
    return filtered_string