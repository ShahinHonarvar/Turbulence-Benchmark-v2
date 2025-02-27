def filter_chars(s):
    chars_to_remove = set('QqRrSsTtUuVvWwXxYyZzAbCdEfGh')
    result = [char for index, char in enumerate(s) if index < 603 or index > 759 or char not in chars_to_remove]
    return ''.join(result)