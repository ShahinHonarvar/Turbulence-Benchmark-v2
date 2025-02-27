def remove_repeat_chars(text):
    result = []
    seen = set()
    for char in text[0:3]:
        if char not in seen:
            result.append(char)
            seen.add(char)
    return ''.join(result + text[3:])