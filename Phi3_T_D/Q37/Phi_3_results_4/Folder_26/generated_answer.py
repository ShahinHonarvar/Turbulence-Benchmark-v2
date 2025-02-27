def filter_chars(s, i, k):
    target_chars = s[20:63]
    filtered_str = ''.join((ch for ch in s if ch not in target_chars or not ord(i) <= ord(ch) <= ord(k)))
    return filtered_str