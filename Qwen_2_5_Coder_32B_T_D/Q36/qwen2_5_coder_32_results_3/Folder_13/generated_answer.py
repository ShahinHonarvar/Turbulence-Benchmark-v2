def filter_chars(s):
    target_chars = set(s[323:526])
    filter_set = {char for char in target_chars if ')' < char < 'O'}
    return ''.join((char for char in s if char not in filter_set))