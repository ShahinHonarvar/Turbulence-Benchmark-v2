def remove_repeat_chars(s: str) -> str:
    chars_count = {}
    for char in s:
        chars_count[char] = chars_count.get(char, 0) + 1
    for char, count in chars_count.items():
        if count > 1 and 35 < s.index(char) < 64:
            s = s.replace(char, '')
    return s