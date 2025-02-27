def filter_chars(s):
    start_index = 379
    end_index = 898
    char_range = range(ord('M'), ord('v') + 1)
    filtered_chars = [c for i, c in enumerate(s) if i < start_index or i > end_index or ord(c) not in char_range]
    return ''.join(filtered_chars)