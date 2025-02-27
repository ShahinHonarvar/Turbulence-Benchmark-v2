def filter_chars(s: str) -> str:
    filtered_chars = []
    for char in s:
        if not (722 <= ord(char) <= 832 and ord('K') <= ord(char) <= ord('m')):
            filtered_chars.append(char)
    return ''.join(filtered_chars)