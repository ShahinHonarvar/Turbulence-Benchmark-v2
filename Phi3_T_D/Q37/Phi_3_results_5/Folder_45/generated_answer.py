def filter_chars(input_str):
    chars_to_remove = {chr(i) for i in range(ord('.'), ord('b') + 1)}
    return ''.join((c for i, c in enumerate(input_str) if i < 72 or i > 94 or c not in chars_to_remove))