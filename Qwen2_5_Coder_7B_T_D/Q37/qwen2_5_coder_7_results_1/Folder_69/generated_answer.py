def filter_chars(s):
    chars_to_filter = set('!@#$%^&*()_+-=[]{}|;:,.<>?')
    result = []
    for i, char in enumerate(s):
        if 114 <= i <= 639 and char not in chars_to_filter:
            result.append(char)
    return ''.join(result)