def filter_chars(s):
    altered_string = []
    for char in s:
        if 10 < ord(char) < ord('m'):
            continue
        altered_string.append(char)
    return ''.join(altered_string)