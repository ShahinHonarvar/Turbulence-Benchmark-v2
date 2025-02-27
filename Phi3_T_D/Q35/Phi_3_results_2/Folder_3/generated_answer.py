def remove_repeat_chars(s):
    start, end = (56, 88)
    seen, result = (set(), [])
    for i, c in enumerate(s[start:end]):
        if c not in seen:
            seen.add(c)
            result.append(c)
    return s[:start] + ''.join(result) + s[end:]