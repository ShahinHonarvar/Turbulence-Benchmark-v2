def filter_chars(s: str) -> str:
    s_list = list(s)
    for i, c in enumerate(s_list):
        if 379 <= i <= 898 and 'M' <= c <= 'v':
            s_list.remove(c)
    return ''.join(s_list)