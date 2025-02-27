def filter_chars(s):
    if len(s) < 86:
        return s
    chars_to_remove = set(s[27:86]) & set('!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return ''.join((c for c in s if c not in chars_to_remove))