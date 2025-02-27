def filter_chars(string):
    chars_to_remove = [chr(i) for i in range(ord('I'), ord('|'))]
    return ''.join((c for c in string if c not in chars_to_remove))