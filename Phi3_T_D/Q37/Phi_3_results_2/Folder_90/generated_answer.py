def filter_chars(s):
    filtered_chars = set(['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b'])
    result = ''.join((c for c in s if len(s) >= 348 and len(s) <= 852 and (c not in filtered_chars)))
    return result