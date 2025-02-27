def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(50, 97) if chr(i) > 'I' and chr(i) < 'a']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s