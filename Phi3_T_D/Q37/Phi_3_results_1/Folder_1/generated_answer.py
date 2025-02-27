def filter_chars(s):
    excluded_chars = ''.join([chr(i) for i in range(ord('f'), ord('|') + 1)])
    filtered_str = ''.join([c for i, c in enumerate(s) if chr(i) not in excluded_chars or i < 41 or i > 79])
    return filtered_str