def filter_chars(s):
    chars_to_remove = set(range(ord(':'), ord('r') + 1))
    result = [c for i, c in enumerate(s) if i < 38 or i > 54 or ord(c) not in chars_to_remove]
    return ''.join(result)