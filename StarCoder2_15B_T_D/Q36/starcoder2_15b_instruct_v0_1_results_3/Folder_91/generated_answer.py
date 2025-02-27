def filter_chars(s: str) -> str:
    removed_chars = []
    for i, c in enumerate(s):
        if i >= 0 and i < 3 and (ord(c) > ord('$')) and (ord(c) < ord('?')):
            removed_chars.append(c)
    for c in removed_chars:
        s = s.replace(c, '')
    return s