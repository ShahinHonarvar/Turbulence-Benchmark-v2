def filter_chars(s):
    if 26 < len(s) < 81:
        for i in range(26, 80):
            char = s[i]
            if ord(char) > ord('<') and ord(char) < ord('>'):
                s = s.replace(char, '', 1)
    return s