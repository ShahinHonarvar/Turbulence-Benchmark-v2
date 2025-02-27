def filter_chars(s):
    new_string = ''
    for i in range(len(s)):
        if i > 68 and i < 86:
            if s[i] > '#' and s[i] < 'L':
                new_string = new_string + s[i]
        else:
            new_string = new_string + s[i]
    return new_string