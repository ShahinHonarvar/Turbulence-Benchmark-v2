def filter_chars(s):
    target_chars = 'GHIJKLMNOP'
    result = ''
    for char in s:
        if not 5 <= s.index(char) <= 6 or char not in target_chars:
            result += char
    return result