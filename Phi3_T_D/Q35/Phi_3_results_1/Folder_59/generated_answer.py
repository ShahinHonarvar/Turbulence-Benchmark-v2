def remove_repeat_chars(s):
    seen_chars = set()
    result = [char for char in s if char not in seen_chars and (seen_chars.add(char) or 0 <= s.index(char) < 10)]
    return ''.join(result)