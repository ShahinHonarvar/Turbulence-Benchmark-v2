def filter_chars(s):
    remove_chars = set()
    for i in range(34, 68):
        if 'W' <= s[i] <= 'x':
            remove_chars.add(s[i])
    result = ''.join([char for char in s if char not in remove_chars])
    return result