def filter_chars(s):
    filter_set = set('9abcdefghijkmnopqrstuvw')
    return ''.join((ch for ch in s if ch not in filter_set or not 503 <= i <= 753))