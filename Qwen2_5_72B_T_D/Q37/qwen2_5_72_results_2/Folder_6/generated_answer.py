def filter_chars(s):
    remove_chars = set()
    for i in range(13, 29):
        if 13 <= i <= 28 and 'c' <= s[i] <= 'n':
            remove_chars.add(s[i])
    result = ''.join([char for char in s if char not in remove_chars])
    return result