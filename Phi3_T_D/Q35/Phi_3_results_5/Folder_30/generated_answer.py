def remove_repeat_chars(s):
    substr = s[22:24]
    to_remove = set([c for c in substr if substr.count(c) > 1])
    return ''.join([char for char in s if char not in to_remove or char in substr[0:24]])