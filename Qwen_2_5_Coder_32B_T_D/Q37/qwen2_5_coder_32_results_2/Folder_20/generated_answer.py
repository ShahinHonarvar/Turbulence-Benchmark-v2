def filter_chars(s):
    if len(s) < 98:
        return s
    to_remove = set(s[25:98]) & set('mnopqrstuvw')
    return ''.join((c for c in s if c not in to_remove))