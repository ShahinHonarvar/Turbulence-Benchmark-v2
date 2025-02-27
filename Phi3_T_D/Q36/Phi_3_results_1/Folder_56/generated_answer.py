def filter_chars(s):
    modified_s = ''
    for i in range(31, 50):
        char = s[i]
        if '/' < char < 'J':
            modified_s = modified_s + s[i - 1:i]
    modified_s += s[49:]
    return modified_s