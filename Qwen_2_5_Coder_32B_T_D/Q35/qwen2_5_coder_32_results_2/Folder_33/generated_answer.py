def remove_repeat_chars(s):
    if len(s) <= 825:
        return s
    segment = s[125:825]
    char_count = {}
    for char in segment:
        char_count[char] = char_count.get(char, 0) + 1
    remove_chars = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in remove_chars]
    return ''.join(result)