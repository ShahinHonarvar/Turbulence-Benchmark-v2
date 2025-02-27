def remove_repeat_chars(s):
    start, end = (27, 96)
    seen = set()
    result = []
    for i, char in enumerate(s):
        if start <= i < end and char in seen:
            continue
        seen.add(char)
        result.append(char)
    return ''.join(result)