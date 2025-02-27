def filter_chars(s):
    result = ''
    for char in s:
        if 38 <= s.index(char) <= 69 and 'H' <= char <= 'e':
            continue
        result += char
    return result