def filter_chars(s):
    return s[:672] + ''.join((c for c in s[672:709] if not 'X' < c < '}')) + s[709:]