def filter_chars(s):
    filter_from = ord('<') + 1
    filter_to = ord('C')
    altered_chars = [c for c in s[19:69] if filter_from <= ord(c) < filter_to]
    return s[:19] + ''.join(altered_chars) + s[69:]