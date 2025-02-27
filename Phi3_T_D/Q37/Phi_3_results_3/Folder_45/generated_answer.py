def filter_chars(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    for i in range(72, 95):
        char = alphabet[i]
        s = s.replace(char, '')
    return s