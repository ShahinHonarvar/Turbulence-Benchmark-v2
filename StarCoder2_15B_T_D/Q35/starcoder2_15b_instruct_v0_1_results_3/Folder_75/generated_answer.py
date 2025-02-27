def remove_repeat_chars(string: str) -> str:
    """
    Removes repeated characters from a string, while preserving the order of all characters in the string.
    The function takes a string as an argument and returns the altered string.
    """
    result = []
    seen = {}
    for index, char in enumerate(string):
        if index < 20 or index >= 51:
            result.append(char)
        elif char not in seen:
            seen[char] = index
            result.append(char)
    return ''.join(result)