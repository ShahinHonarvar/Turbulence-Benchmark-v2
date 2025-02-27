def filter_chars(s):
    start_index = min(38, len(s))
    end_index = min(54, len(s))
    chars_to_remove = set([chr(i) for i in range(ord(':'), ord('r') + 1)])
    return ''.join([c for i, c in enumerate(s) if i < start_index or i > end_index or c not in chars_to_remove])