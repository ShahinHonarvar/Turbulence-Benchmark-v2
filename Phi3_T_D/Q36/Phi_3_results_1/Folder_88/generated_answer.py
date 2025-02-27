def filter_chars(string):
    for character in string[78:81]:
        if 'S' < character < '[':
            string = string.replace(character, '')
    return string