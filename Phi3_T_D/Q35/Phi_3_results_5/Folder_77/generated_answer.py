def remove_repeat_chars(s):
    substr = s[355:988]
    seen = set()
    result = []
    repeated = set()
    for char in substr:
        if char in seen:
            repeated.add(char)
        seen.add(char)
    for char in s:
        if char not in repeated:
            result.append(char)
    return ''.join((result[:355] + substr.replace(char, '') for char in repeated)) + ''.join(result[988:])