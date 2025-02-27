def filter_chars(s):
    to_remove = set([ch for ch in s[1:9] if '8' < ch < 'm'])
    return ''.join([ch for ch in s if ch not in to_remove])