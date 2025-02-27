def filter_chars(s):
    c = chr
    return ''.join((ch for ch in s if ch != c(38) and ch != c(69) and (not c(65) <= ch <= c(99))))