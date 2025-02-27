def filter_chars(s):
    chars_to_remove = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ:;<=>?@[]^_`{|}~')
    result = []
    for i, char in enumerate(s):
        if 12 <= i <= 77 and char in chars_to_remove:
            continue
        result.append(char)
    return ''.join(result)