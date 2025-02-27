def filter_chars(text: str) -> str:
    result = ''
    for char in text:
        if not (char.isalpha() and 27 <= ord(char) - ord('a') <= 85 and (ord('c') <= ord(char) <= ord('i'))):
            result += char
    return result