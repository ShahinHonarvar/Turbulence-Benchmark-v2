def filter_chars(s):
    chars_to_remove = [char for char in s[3:6] if 'Y' < char < 's']
    result = ''.join([char for char in s if char not in chars_to_remove])
    return result