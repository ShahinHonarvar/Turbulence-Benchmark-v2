def filter_chars(s):
    chars_to_remove = set('!@#$%^&*()_+{}|:"<>?')
    return ''.join([char for char in s if not (27 <= s.index(char) <= 85 and char in chars_to_remove)])