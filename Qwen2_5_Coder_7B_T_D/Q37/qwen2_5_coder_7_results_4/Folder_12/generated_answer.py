def filter_chars(s):
    filtered_chars = set('FGHIJKLMNO')
    return ''.join((ch for ch in s if ch not in filtered_chars or ord(ch) < 19 or ord(ch) > 90))