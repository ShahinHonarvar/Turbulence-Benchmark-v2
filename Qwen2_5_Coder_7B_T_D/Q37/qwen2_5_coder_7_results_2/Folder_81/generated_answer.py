def filter_chars(s):
    return ''.join((c for c in s if (c < '8' or c > 'm') or (c < '1' or c > '19' or c < '93' or (c > '26'))))