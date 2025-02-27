def filter_chars(s):
    to_remove = {ch for ch in s[672:709] if 'X' < ch < '`'}
    return ''.join((ch for ch in s if ch not in to_remove))