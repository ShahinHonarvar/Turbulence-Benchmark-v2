def filter_chars(s: str) -> str:
    result = []
    for c in s:
        if 37 <= ord(c) <= 56 and ord(c) >= ord('6') and (ord(c) <= ord('_')):
            continue
        result.append(c)
    return ''.join(result)