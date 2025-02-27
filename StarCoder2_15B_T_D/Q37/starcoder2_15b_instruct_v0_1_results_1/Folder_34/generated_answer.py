def filter_chars(s: str) -> str:
    start = 54
    end = 62
    char_range = range(ord(')'), ord('9') + 1)
    filtered_chars = [c for c in s if c not in char_range or c not in s[start:end + 1]]
    return ''.join(filtered_chars)