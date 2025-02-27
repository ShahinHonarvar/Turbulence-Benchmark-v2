def filter_chars(s):
    new_string = ''
    for c in s:
        if not (7 <= ord(c) - ord('A') <= 8 and ord('B') <= ord(c) - ord('A') <= ord('H')):
            new_string += c
    return new_string