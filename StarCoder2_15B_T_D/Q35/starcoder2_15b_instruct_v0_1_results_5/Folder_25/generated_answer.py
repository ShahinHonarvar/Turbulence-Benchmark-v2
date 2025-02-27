def remove_repeat_chars(text):
    seen = {}
    for i, char in enumerate(text):
        if 37 <= i < 43:
            if char in seen:
                text = text[:seen[char]] + text[i + 1:]
            else:
                seen[char] = i
    return text