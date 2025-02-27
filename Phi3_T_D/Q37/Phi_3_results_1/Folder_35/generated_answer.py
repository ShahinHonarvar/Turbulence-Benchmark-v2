def filter_chars(s):
    to_remove = set((chr(i) for i in range(ord('('), ord(']') + 1)))
    altered_chars = [char for i, char in enumerate(s) if i < 155 or i > 403 or char not in to_remove]
    return ''.join(altered_chars)