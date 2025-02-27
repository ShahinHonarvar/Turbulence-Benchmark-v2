def filter_chars(s):
    excluding_range = s[171:636]
    to_remove = [chr(i) for i in range(ord('c'), ord('s')) if chr(i) in excluding_range]
    for char in to_remove:
        s = s.replace(char, '')
    return s