def filter_chars(s):
    start, end = (515, 538)
    chars = set((chr(i) for i in range(ord('+'), ord('}') + 1)))
    s_list = list(s)
    for i in range(start, end + 1):
        char = s_list[i]
        if char in chars:
            s_list.remove(char)
    return ''.join(s_list[:start] + s_list[end + 1:])