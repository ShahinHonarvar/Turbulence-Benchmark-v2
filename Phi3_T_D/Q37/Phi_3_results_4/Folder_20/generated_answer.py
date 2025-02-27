def filter_chars(s):
    s_list = list(s)
    to_remove = (ord(c) for c in s[25:97] if 'm' <= c <= 'w')
    s_list = [c for c in s_list if ord(c) not in to_remove]
    return ''.join(s_list)