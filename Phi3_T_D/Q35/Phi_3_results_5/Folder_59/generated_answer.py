def remove_repeat_chars(s: str) -> str:
    result = []
    seen = set()
    for i in range(11):
        c = s[i]
        if c in seen:
            continue
        seen.add(c)
        result.append(c)
    return ''.join(result)