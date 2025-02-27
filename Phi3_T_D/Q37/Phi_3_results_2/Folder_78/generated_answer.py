def filter_chars(s):
    altered = []
    for index, char in enumerate(s[75:100]):
        if '8' <= char <= 'e':
            continue
        altered.append(char)
    return s[:75] + ''.join(altered) + s[100:]