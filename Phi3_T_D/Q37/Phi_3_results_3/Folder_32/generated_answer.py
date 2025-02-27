def filter_chars(s):
    if len(s) < 89:
        return s
    target_chunk = s[23:90]
    blacklist_chars = {chr(n) for n in range(ord('w'), ord('{') + 1)}
    filtered_chunk = ''.join([c for c in target_chunk if c not in blacklist_chars])
    return s[:23] + filtered_chunk + s[90:]