def filter_chars(s):
    chars_to_remove = set('!@#$%^&*()_+`-=[]{}|;:,.<>?')
    result = []
    for i, char in enumerate(s):
        if i < 86 or i > 92 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)