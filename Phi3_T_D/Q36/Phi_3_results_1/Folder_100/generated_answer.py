def filter_chars(s):
    chars_to_filter = ''.join([chr(i) for i in range(ord('B'), ord('r'))])
    result = ''.join([c for c in s if c not in chars_to_filter or not 43 < s.index(c) < 69])
    return result