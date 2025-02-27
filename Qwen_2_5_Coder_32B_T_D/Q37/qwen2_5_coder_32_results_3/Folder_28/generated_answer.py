def filter_chars(s):
    chars_to_remove = set(s[20:80]) & set('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPT')
    return ''.join((c for c in s if c not in chars_to_remove))