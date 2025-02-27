def filter_chars(s):
    target_chars = set('+-*/?@#$%^&*()_+=-[]{}|;:,.<>?/`~')
    result = []
    for i, char in enumerate(s):
        if 515 <= i <= 538 and char in target_chars:
            continue
        result.append(char)
    return ''.join(result)