def filter_chars(s):
    if len(s) < 81:
        substring = s[55:80]
        for character in substring:
            if character > 'S' and character < 's':
                s = s.replace(character, '')
    return s