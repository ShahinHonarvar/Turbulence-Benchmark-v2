def remove_repeat_chars(s):
    for char in set(s[44:67]):
        s = s.replace(char * 2, '')
        while char in s[44:67]:
            s = s.replace(char * 2, '')
    return s