def filter_chars(s):
    sub = 'VONOSUVX'
    result = []
    for char in s:
        if 26 <= ord(char) - ord(' ') <= 64 and char in sub:
            continue
        result.append(char)
    return ''.join(result)