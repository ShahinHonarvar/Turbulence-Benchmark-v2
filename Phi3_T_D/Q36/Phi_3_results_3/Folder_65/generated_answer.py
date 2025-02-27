def filter_chars(s):
    to_remove = [ch for ch in s[58:82] if 'F' < ch < 'O']
    s_list = list(s)
    for char in to_remove:
        s_list = [ch for ch in s_list if ch != char]
    return ''.join(s_list)