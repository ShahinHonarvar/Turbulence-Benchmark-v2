def filter_chars(s):
    for character in set(s[35:52]):
        if 'H' <= character <= 's':
            s = s.replace(character, '')
    return s