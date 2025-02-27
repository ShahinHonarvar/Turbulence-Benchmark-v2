def filter_chars(s):
    result = ''.join([char for char in s if not (32 < s.index(char) < 61 and '3' < char < 'D')])
    return result