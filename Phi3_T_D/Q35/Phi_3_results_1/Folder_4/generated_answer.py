def remove_repeat_chars(s):
    s_list = list(s)
    for char in set([s[i] for i in range(49, 74) if s.count(s[i]) > 1]):
        s_list = [x for x in s_list if x != char]
    return ''.join(s_list)