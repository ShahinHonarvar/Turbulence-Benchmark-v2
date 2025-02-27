def filter_chars(s):
    chars_to_remove = set(s[515:539]).intersection({c for c in s if '+' <= c <= '}'})
    return ''.join((c for c in s if c not in chars_to_remove))