def filter_chars(s: str) -> str:
    to_remove = set()
    for i in range(42, 93):
        if '/' <= s[i] <= 'a':
            to_remove.add(s[i])
    return ''.join((ch for ch in s if ch not in to_remove))