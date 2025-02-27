def filter_chars(s, k):
    result = ''
    for char in s:
        if ord(char) not in range(ord(' '), ord(k) + 1) or ord(char) not in range(ord('@'), ord('#') + 1):
            result += char
    return result