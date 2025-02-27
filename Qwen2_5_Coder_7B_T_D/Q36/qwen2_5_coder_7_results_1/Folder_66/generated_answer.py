def filter_chars(s):
    chars_to_remove = set()
    for i in range(40, 87):
        char = chr(i)
        if '!' < char < '}':
            chars_to_remove.add(char)
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result