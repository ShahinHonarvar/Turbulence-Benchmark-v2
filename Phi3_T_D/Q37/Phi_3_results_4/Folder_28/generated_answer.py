def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('!'), ord('T') + 1)]
    altered_chars = [char for idx, char in enumerate(s) if idx < 20 or idx > 79 or char not in target_chars]
    return ''.join(altered_chars)