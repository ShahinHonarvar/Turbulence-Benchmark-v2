def filter_chars(s):
    to_remove = set(s[348:853]).intersection({chr(i) for i in range(ord('J'), ord('b') + 1)})
    return ''.join((c for c in s if c not in to_remove))