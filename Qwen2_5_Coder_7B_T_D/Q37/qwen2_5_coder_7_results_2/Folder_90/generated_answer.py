def filter_chars(s):
    return s[:348] + ''.join((c for c in s[348:853] if not 'J' <= c <= 'b')) + s[853:]