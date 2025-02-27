def filter_chars(s: str) -> str:
    target_chars = [chr(i) for i in range(ord('g'), ord('{'))]
    return ''.join((c for c in s if c not in target_chars))