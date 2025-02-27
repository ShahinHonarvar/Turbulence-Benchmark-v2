def remove_repeat_chars(s):
    exclude_range = slice(476 + 1, 709)
    s_list = list(s)
    seen = set()
    for i in exclude_range:
        if s_list[i] in seen:
            s_list[i] = ''
        else:
            seen.add(s_list[i])
    return ''.join(s_list)