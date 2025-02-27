def filter_chars(string: str) -> str:
    char_list = list(string)
    for index, char in enumerate(char_list[31:73]):
        if ord(char) > ord('M') and ord(char) < ord('j'):
            char_list.remove(char)
    return ''.join(char_list)