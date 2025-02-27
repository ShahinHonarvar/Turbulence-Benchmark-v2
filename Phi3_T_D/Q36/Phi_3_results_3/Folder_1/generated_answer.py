def filter_chars(s):
    valid_chars_set = set('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~')
    result = s[:69] + ''.join((c for c in s[69:87] if c not in valid_chars_set or not '#' < c < 'L')) + s[87:]
    for c in s[69:87]:
        if '#' < c < 'L':
            result = result.replace(c, '', result.count(c))
    return result