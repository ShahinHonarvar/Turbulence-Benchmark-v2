def filter_chars(s):
    target_chars = set()
    for i in range(82, 93):
        char = chr(i)
        if '!' < char < '*':
            target_chars.add(char)
    for char in target_chars:
        s = s.replace(char, '')
    return s