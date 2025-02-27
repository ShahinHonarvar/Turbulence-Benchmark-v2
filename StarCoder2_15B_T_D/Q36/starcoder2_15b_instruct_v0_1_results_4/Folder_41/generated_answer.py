def filter_chars(string):
    chars_to_remove = {chr(ord('f') + i) for i in range(1, 10)}
    result = [c for c in string if c not in chars_to_remove]
    return ''.join(result)