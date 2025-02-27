def filter_chars(s):
    return ''.join((c for c in s if not 11 <= ord(c) <= ord('v')))