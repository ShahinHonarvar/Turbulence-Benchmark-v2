def filter_chars(s):
    target_chars = set(s[42:98]) & set('*"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz')
    return ''.join((c for c in s if c not in target_chars))