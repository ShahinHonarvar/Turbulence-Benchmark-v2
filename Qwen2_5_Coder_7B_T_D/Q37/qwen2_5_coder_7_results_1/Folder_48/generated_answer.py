def filter_chars(s):
    return ''.join((ch for ch in s if not (513 <= s.find(ch) <= 877 and '?' <= ch <= 'n')))