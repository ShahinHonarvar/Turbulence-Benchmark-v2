def filter_chars(s):
    chars_to_remove = set(s[43:81]) & set('=*+,-./0123456789:;<=>?@ABCDE')
    return ''.join([char for char in s if char not in chars_to_remove])