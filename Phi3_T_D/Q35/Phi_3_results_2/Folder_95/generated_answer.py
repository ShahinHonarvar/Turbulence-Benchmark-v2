def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, char in enumerate(s):
        if 32 < ord(char) < 99 and char not in seen:
            seen.add(char)
        elif 32 < ord(char) < 99 and char in result:
            while char in result:
                result.remove(char)
    return ''.join(result)