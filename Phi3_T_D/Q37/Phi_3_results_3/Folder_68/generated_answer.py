def filter_chars(s):
    target = '6789:;<=.-=_+)(*&^%$#@!~`{|}[]'
    s = ''.join([char for char in s if char not in target[7:10]])
    return s