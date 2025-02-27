def filter_chars(s):
    filtered_chars = [char for i, char in enumerate(s) if 72 < ord(char) < 93]
    for char in set(filtered_chars):
        s = s.replace(char, '')
    return s