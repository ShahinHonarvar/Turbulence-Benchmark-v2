def filter_chars(s):
    if len(s) <= 759:
        chars_to_remove = set(s[603:760]) & set('QhRSTUVWXYZabcdefg')
    else:
        chars_to_remove = set(s[603:760]) & set('QhRSTUVWXYZabcdefg')
    return ''.join([c for c in s if c not in chars_to_remove])