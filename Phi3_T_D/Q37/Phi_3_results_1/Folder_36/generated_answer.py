def filter_chars(s):
    start_idx, end_idx = (259, 502)
    to_remove = set((chr(c) for c in range(ord(','), ord('3') + 1)))
    s_list = list(s)
    for i in range(start_idx, min(end_idx + 1, len(s_list))):
        if s_list[i] in to_remove:
            s_list[i] = ''
    return ''.join(s_list)