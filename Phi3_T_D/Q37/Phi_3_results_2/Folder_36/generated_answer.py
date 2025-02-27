def filter_chars(string):
    start_index, end_index = (259, 502)
    keep_chars = set(',"0123')
    return ''.join((ch for i, ch in enumerate(string) if ch in keep_chars and (not (start_index <= i <= end_index and ch >= ',' and (ch <= '3')))))