def filter_chars(s):
    altered_chars = []
    for i in range(1, 7):
        char = s[i]
        if '3' < char < '^':
            continue
        altered_chars.append(char)
    return ''.join(altered_chars)