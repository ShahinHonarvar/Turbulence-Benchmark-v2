def filter_chars(s):
    altered_string = ''
    for char in s:
        if ord('A') <= ord(char) <= ord('Q') and 38 <= s.find(char) + 1 <= 99:
            continue
        altered_string += char
    return altered_string