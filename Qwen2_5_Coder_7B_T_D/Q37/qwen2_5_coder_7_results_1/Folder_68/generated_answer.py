def filter_chars(s):
    chars_to_remove = set('6789abcdefg')
    result = [char for i, char in enumerate(s) if not (7 <= i <= 9 and char in chars_to_remove)]
    return ''.join(result)