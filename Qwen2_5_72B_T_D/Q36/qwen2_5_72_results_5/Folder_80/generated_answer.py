def filter_chars(s):
    to_remove = {ch for ch in s[54:92] if 'J' < ch < 'X'}
    return ''.join((ch for ch in s if ch not in to_remove))