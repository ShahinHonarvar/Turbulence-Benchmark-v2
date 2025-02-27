def filter_chars(s):
    filtered_chars = [c for c in s[164:707] if not 'O' <= c <= '}']
    return s[:164] + ''.join(filtered_chars) + s[707:]