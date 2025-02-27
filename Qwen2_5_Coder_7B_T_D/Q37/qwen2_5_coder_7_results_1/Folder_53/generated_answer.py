def filter_chars(s):
    s = list(s)
    chars_to_remove = set('abcdefghij')
    for i in range(len(s)):
        if 83 <= i <= 99 and s[i] in chars_to_remove:
            s[i] = ''
    return ''.join(s)