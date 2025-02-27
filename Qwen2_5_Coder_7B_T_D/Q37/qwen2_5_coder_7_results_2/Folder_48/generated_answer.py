def filter_chars(s):
    return ''.join((c for c in s if not (513 <= s.find(c) <= 877 and '?' <= c <= 'n')))