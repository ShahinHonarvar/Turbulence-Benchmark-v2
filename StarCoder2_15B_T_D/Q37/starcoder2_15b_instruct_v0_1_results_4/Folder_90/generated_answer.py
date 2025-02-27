def filter_chars(s: str) -> str:
    chars_to_remove = set()
    for i, c in enumerate(s):
        if 348 <= i <= 852 and ord('J') <= ord(c) <= ord('b'):
            chars_to_remove.add(c)
    return ''.join((c for c in s if c not in chars_to_remove))