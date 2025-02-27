def filter_chars(s):
    result = ''
    for char in s:
        ascii_val = ord(char)
        if 90 < ascii_val < 97 or ascii_val > ord('w'):
            continue
        result += char
    return result