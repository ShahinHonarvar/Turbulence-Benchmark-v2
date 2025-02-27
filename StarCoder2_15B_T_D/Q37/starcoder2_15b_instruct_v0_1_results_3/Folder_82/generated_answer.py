def filter_chars(text: str) -> str:
    filtered_text = ''
    for character in text:
        if ord(character) >= ord('P') and ord(character) <= ord('x') or (ord(character) >= ord('P') and ord(character) <= ord('x')):
            continue
        else:
            filtered_text += character
    return filtered_text