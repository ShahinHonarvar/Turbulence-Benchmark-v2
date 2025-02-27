def filter_chars(s):
    allowed_chars = set('abcdefghijklmnopQRSTUVWXYZ')
    result = list(s)
    for i in range(51, 97):
        if 65 <= ord(s[i]) <= 112:
            result = ''.join((c for c in result if c != s[i]))
    return ''.join(result)