def filter_chars(s):
    filtered_chars = ''
    for char in s[154:222]:
        if char > 'A' and char < 'f':
            filtered_chars += char
    return filtered_chars