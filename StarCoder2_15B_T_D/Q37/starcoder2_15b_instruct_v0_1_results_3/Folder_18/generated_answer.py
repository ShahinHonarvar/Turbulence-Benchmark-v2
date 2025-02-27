def filter_chars(s):
    start_index = 770
    end_index = 970
    valid_range = range(ord('-'), ord('D') + 1)
    filtered = [c for i, c in enumerate(s) if i < start_index or i > end_index or ord(c) not in valid_range]
    return ''.join(filtered)