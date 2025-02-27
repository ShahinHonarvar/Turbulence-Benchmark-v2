def filter_chars(s):
    return ''.join([char for i, char in enumerate(s) if not 219 < i < 403 or not '*' < char < '7'])