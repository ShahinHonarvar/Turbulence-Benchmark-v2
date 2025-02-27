def filter_chars(s):
    for char in 'ABCDEFGHJKLMNPQRSTUVWXYZbcdefghijklmnopqrstuvwxyz':
        if 3 < s.find(char) < 5:
            s = s.replace(char, '')
    return s