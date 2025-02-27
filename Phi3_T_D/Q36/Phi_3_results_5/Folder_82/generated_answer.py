def filter_chars(s):
    target_chars = 'NOPQRS'
    new_s = ''
    for c in s:
        if ord('V') < ord(c) < ord('j') and c in target_chars:
            continue
        new_s += c
    return new_s