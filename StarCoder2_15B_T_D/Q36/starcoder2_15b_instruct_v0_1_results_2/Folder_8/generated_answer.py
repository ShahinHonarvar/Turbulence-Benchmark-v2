def filter_chars(text: str) -> str:
    filtered = ''
    for i, c in enumerate(text):
        if i >= 82 and i < 93 and (ord(c) > ord('!')) and (ord(c) < ord('*')):
            continue
        filtered += c
    return filtered