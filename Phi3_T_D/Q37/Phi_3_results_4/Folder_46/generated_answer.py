def filter_chars(s):
    start_idx = 11
    end_idx = 72
    return ''.join([c for i, c in enumerate(s) if not (start_idx <= i <= end_idx and 'i' <= c <= 'v')])