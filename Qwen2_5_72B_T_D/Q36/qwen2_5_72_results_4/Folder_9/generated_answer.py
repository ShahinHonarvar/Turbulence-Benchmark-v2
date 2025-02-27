def filter_chars(s):
    to_remove = set([ch for ch in s[50:92] if 'A' < ch < 'Q'])
    return ''.join([ch for ch in s if ch not in to_remove])