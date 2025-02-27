def filter_chars(s):
    for i in range(1, 7):
        if '-' < s[i] < 'L':
            s = ''.join([char for char in s if char != s[i]])
    return s