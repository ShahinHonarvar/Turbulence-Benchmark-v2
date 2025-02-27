def filter_chars(s):
    for char in '?' + string.ascii_lowercase[:ord('f') - ord('?') + 1] + ' ':
        s = s.replace(char, '', 1)
    return s