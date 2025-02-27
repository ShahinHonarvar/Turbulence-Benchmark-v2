def filter_chars(s):
    chars_to_remove = set(s[770:971]).intersection({c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ-0123456789' if '-' <= c <= 'D'})
    return ''.join((c for c in s if c not in chars_to_remove))