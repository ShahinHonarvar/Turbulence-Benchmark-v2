def filter_chars(s):
    s_list = list(s)
    to_remove = set()
    for i in range(31, 73):
        if 'M' < s[i] < 'j':
            to_remove.add(s[i])
    result = [char for char in s_list if char not in to_remove]
    return ''.join(result)