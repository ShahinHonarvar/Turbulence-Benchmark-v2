def filter_chars(s: str) -> str:
    output = []
    for c in s:
        if not 10 <= ord(c) - ord('I') <= 59:
            output.append(c)
    return ''.join(output)