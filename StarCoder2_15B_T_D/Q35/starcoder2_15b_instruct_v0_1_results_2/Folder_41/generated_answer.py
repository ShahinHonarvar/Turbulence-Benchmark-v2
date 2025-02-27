def remove_repeat_chars(s):
    chars = [ch for ch in s]
    for ch in set(s[3:8]):
        if s.count(ch) > 1:
            while ch in chars:
                chars.remove(ch)
    return ''.join(chars)