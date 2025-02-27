def filter_chars(s):
    relevant_chars = s[18:38]
    filtered_chars = ''.join([c for c in s if c not in relevant_chars or ord(c) > ord(')') or ord(c) >= ord('P')])
    return filtered_chars