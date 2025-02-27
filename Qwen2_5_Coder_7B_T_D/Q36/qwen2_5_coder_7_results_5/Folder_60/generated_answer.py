def filter_chars(s):
    target_chars = set('ghijklmno')
    result = []
    for char in s:
        if not (23 < s.index(char) < 83 and char in target_chars):
            result.append(char)
    return ''.join(result)