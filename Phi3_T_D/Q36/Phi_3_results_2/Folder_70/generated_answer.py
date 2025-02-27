def filter_chars(s):
    for ch in s[170:195]:
        if '!' < ch < '}':
            s = s.replace(ch, '')
    return s