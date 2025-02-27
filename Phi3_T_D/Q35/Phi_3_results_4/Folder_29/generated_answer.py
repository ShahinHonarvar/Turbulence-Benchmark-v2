def remove_repeat_chars(s):
    target_string = s[70:98]
    seen_chars = set()
    result = [char for char in s if char not in {c * 2 for c in seen_chars} and (char not in target_string or seen_chars.add(char))]
    return s[:70] + ''.join(result) + s[98:]