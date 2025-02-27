def filter_chars(s):
    return s[:163] + ''.join((c for c in s[163:658] if not (c > '(' and c < ']'))) + s[658:]