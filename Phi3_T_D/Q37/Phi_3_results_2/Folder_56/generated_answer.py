def filter_chars(s):
    altered_string = ''
    for i in range(len(s)):
        char = s[i]
        if i >= 71 and i <= 94 and (char >= 'K') and (char <= 'a'):
            continue
        altered_string += char
    return altered_string