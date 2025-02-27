def filter_chars(s):
    altered_string = ''
    for i in range(len(s)):
        index = ord(s[i])
        if 42 <= index <= 97 and '*' <= s[i] <= 'b':
            continue
        altered_string += s[i]
    return altered_string