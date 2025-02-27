def filter_chars(s):
    remove_chars = set()
    for i in range(71, 95):
        if 75 <= ord(s[i]) <= 97:
            remove_chars.add(s[i])
    result = ''.join([char for char in s if char not in remove_chars])
    return result